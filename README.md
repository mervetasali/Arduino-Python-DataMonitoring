# Arduino-Python-DataMonitoring

A hands-on project series focused on learning serial communication between Arduino and Python while following software engineering and industrial automation principles.

## Project Goal

The purpose of this project is to build a solid foundation for:

* Serial Communication
* Data Monitoring
* Packet Parsing
* Data Validation
* Error Handling
* Warning Management

---

## Current Project

### Arduino System Monitor

Arduino generates temperature data and sends it to Python through serial communication.

Python receives the incoming packets, validates them, and reports the system status.

### Example Packets

Valid packets:

```text
TEMP:45
TEMP:25
TEMP:80
```

Invalid packets:

```text
TEMP:
TEMP:ab
PRESSURE:45
TEMP45
```

---

## Current Version

### v0.3.0

Implemented:

* Serial communication between Arduino and Python
* Communication timeout handling
* Empty packet handling
* Packet parsing
* Packet validation
* Tag validation
* Numeric value validation
* Temperature range validation
* Error code management
* Warning code management
* Arduino packet simulator for communication testing
* Modular project structure
* Git version control workflow

---

## Project Structure

```text
Arduino-Python-DataMonitoring
│
├── DataMonitoring_v0.3.0.py
├── serialHelpers.py
├── config.py
└── Arduino Simulator
```

---

## Example Output

```text
System status: Running, Current TEMP value = 45

System status: Warning,
Warning Code (W-1): The sensor value is too low.

System status: Warning,
Warning Code (W-2): The sensor value is too high.

System status: Error,
Error Code (E-2): The incoming data tag is not TEMP.

System status: Error,
Error Code (E-3): The incoming data value is not valid.
```

