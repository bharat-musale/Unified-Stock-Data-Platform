import time
import logging
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from app.database.connection import db_manager
from app.config import config
from app.services.screener_service import screener_service

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class ScreenerScheduler:
    def __init__(self):
        self.scheduler = BackgroundScheduler(timezone="Asia/Kolkata")

    # ----------------------------------------------------
    # FETCH SYMBOLS
    # ----------------------------------------------------
    def get_all_symbols(self):
        conn = None
        cursor = None
        try:
            conn = db_manager.get_connection(
                config.DB_STOCK_MARKET,
                dict_cursor=True
            )
            cursor = conn.cursor()

            cursor.execute("""
                SELECT symbol
                FROM listed_companies
                ORDER BY id
            """)
            rows = cursor.fetchall()
            return [row["symbol"] for row in rows]

        except Exception as e:
            logger.error(f"❌ Failed to load symbols: {e}", exc_info=True)
            return []

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    # ----------------------------------------------------
    # MAIN JOB
    # ----------------------------------------------------
    def run_daily_screener_job(self):
        symbols = self.get_all_symbols()
        total = len(symbols)

        if total == 0:
            logger.warning("⚠️ No symbols found. Skipping screener job.")
            return

        logger.info(f"🕒 Screener CRON STARTED | Total symbols: {total}")

        success = 0
        failed = 0

        for idx, symbol in enumerate(symbols, start=1):
            try:
                clean_symbol = symbol.replace(".NS", "")

                logger.info(f"[{idx}/{total}] Fetching screener: {clean_symbol}")

                screener_service.fetch_and_save(
                    clean_symbol,
                    "consolidated"
                )

                success += 1
                time.sleep(1.5)  # ⛔ anti-ban (DO NOT REMOVE)

            except Exception as e:
                failed += 1
                logger.error(f"❌ Screener failed for {symbol}: {e}", exc_info=True)

        logger.info(
            f"✅ Screener CRON FINISHED | "
            f"Success: {success} | Failed: {failed} | "
            f"Time: {datetime.now()}"
        )

    # ----------------------------------------------------
    # START
    # ----------------------------------------------------
    def start(self):
        # 🔁 Scheduled run
        self.scheduler.add_job(
            self.run_daily_screener_job,
            trigger="cron",
            hour=2,
            minute=30,
            id="daily_screener_job",
            replace_existing=True,
            max_instances=1
        )

        self.scheduler.start()
        logger.info("🕒 Screener Scheduler started (02:30 AM IST)")

        # ⚡ Immediate startup run
        self.run_daily_screener_job()


# ✅ SINGLE INSTANCE (IMPORTANT)
screener_scheduler = ScreenerScheduler()
