# system_snapshot.py
import subprocess


def run_command(command):
    """Executes a system command and returns its output as a string."""
    result = subprocess.run(
        command, shell=True, capture_output=True, text=True
    )
    return result.stdout.strip()


# 1. Run "uptime" and print it under "=== Uptime ===" header
print("=== Uptime ===")
print(run_command("uptime"))
print()

# 2. Run "df -h" and print it under "=== Disk Usage ===" header
print("=== Disk Usage ===")
print(run_command("df -h"))
print()

# 3. Run "free -h" and print it under "=== Memory Usage ===" header
print("=== Memory Usage ===")
print(run_command("free -h"))
print()

# 4. Check ssh status and print a final summary line
# Using systemctl is-active to check if ssh service is active
ssh_status_output = run_command("systemctl is-active ssh")

if ssh_status_output == "active":
    ssh_state = "ACTIVE"
else:
    ssh_state = "INACTIVE"

print(f"System snapshot complete - SSH: {ssh_state}")