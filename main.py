import threading

import uvicorn
import api
import app
import scheduler

if __name__ == "__main__":
    threading.Thread(target=scheduler.main).start()
    uvicorn.run(app.app, host='0.0.0.0', port=5000, log_level="info")
