import os
import logging
from datetime import datetime

def setup_logger(name, log_dir=None):
    """
    設定並返回 logger
    
    Args:
        name (str): logger 名稱
        log_dir (str, optional): 日誌目錄路徑。如果為 None，則使用預設路徑
    
    Returns:
        logging.Logger: 配置好的 logger 實例
    """
    # 如果沒有指定 log_dir，使用預設路徑
    if log_dir is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        log_dir = os.path.join(base_dir, 'log')
    
    # 確保日誌目錄存在
    os.makedirs(log_dir, exist_ok=True)
    
    # 建立 logger
    logger = logging.getLogger(name)
    
    # 如果 logger 已經有 handlers，直接返回（避免重複設定）
    if logger.handlers:
        return logger
        
    logger.setLevel(logging.INFO)
    
    # 設定日誌格式
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s', 
                                datefmt='%Y-%m-%d %H:%M:%S')
    
    # 檔案 handler
    log_file = os.path.join(log_dir, f'{name}_{datetime.now().strftime("%Y%m%d")}.log')
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # 控制台 handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger
