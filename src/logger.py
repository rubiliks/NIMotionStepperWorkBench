import atexit
import logging
import shutil
from datetime import datetime, timedelta

from app.models.file_system.folder_register import get_document_path


def _cleanup_old_logs(days: int, max_size_gb: float):
    """Очистка старых логов"""
    logs_dir = get_document_path() / "SortingMaster" / "logs"
    cutoff_date = datetime.now() - timedelta(days=days)

    # Удаление по дате
    for day_dir in logs_dir.iterdir():
        if day_dir.is_dir():
            try:
                dir_date = datetime.strptime(day_dir.name, "%Y-%m-%d")
                if dir_date < cutoff_date:
                    shutil.rmtree(day_dir)
            except ValueError:
                continue

    # Удаление по размеру
    max_size_bytes = max_size_gb * 1024 * 1024 * 1024
    day_dirs = []

    for day_dir in logs_dir.iterdir():
        if day_dir.is_dir():
            try:
                dir_date = datetime.strptime(day_dir.name, "%Y-%m-%d")
                dir_size = sum(
                    f.stat().st_size for f in day_dir.rglob("*") if f.is_file()
                )
                day_dirs.append({"path": day_dir, "date": dir_date, "size": dir_size})
            except ValueError:
                continue

    day_dirs.sort(key=lambda x: x["date"], reverse=True)

    total_size = 0
    for dir_info in day_dirs:
        if total_size + dir_info["size"] <= max_size_bytes:
            total_size += dir_info["size"]
        else:
            shutil.rmtree(dir_info["path"])


def _log_session_end():
    """Логирование завершения сессии"""
    logger = logging.getLogger("sortingmaster")
    logger.info("=" * 100)
    logger.info(f"ЗАВЕРШЕНИЕ СЕССИИ - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 100)


def init_logger(
    level: str = "INFO",
    enable_console: bool = True,
    cleanup_days: int = 30,
    max_size_gb: float = 5.0,
):
    """
    Инициализация логгера - вызвать ОДИН раз в начале main()

    Args:
        level: Уровень логирования (DEBUG, INFO, WARNING, ERROR)
        enable_console: Выводить логи в консоль
        cleanup_days: Удалять логи старше N дней
        max_size_gb: Максимальный размер всех логов в GB
    """

    # Создаем папку для текущего дня
    logs_dir = get_document_path() / "SortingMaster" / "logs"
    today_dir = logs_dir / datetime.now().strftime("%Y-%m-%d")
    today_dir.mkdir(parents=True, exist_ok=True)

    # Файл лога для текущей сессии
    session_time = datetime.now().strftime("%H-%M-%S")
    log_file = today_dir / f"app_{session_time}.log"
    error_file = today_dir / "errors_all.log"

    # Формат логов
    detailed_fmt = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)-30s | %(funcName)-20s:%(lineno)-4d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_fmt = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s", datefmt="%H:%M:%S"
    )

    # Настройка root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    root_logger.handlers.clear()

    # Консоль
    if enable_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(console_fmt)
        root_logger.addHandler(console_handler)

    # Файл сессии
    file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    file_handler.setFormatter(detailed_fmt)
    root_logger.addHandler(file_handler)

    # Файл ошибок (общий)
    error_handler = logging.FileHandler(error_file, mode="a", encoding="utf-8")
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(detailed_fmt)
    root_logger.addHandler(error_handler)

    # Логируем старт
    logger = logging.getLogger("sortingmaster")
    logger.info("=" * 100)
    logger.info(f"СТАРТ ПРИЛОЖЕНИЯ - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"Лог-файл: {log_file}")
    logger.info("=" * 100)

    # Очистка старых логов
    try:
        _cleanup_old_logs(cleanup_days, max_size_gb)
    except Exception as e:
        logger.warning(f"Ошибка очистки логов: {e}")

    # Регистрируем завершение
    atexit.register(_log_session_end)