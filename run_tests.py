from datetime import datetime
import subprocess
import os

current_time = datetime.now()
timestamp = datetime.timestamp
timestamp = current_time.strftime("%Y-%m-%d__%H-%M-%S")
print(timestamp)

filename = f"report_{timestamp}.html"
print(filename)

report_path = os.path.join("reports",filename)

subprocess.run([
    "py",
    "-m",
    "pytest",
    "-v",
    "-s",
    f"--html={report_path}"
],
 check =True
)

print(f"\nHTML Report generated at: {report_path}")