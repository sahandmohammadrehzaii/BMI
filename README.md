# BMI Calculator 🏥

A simple and user-friendly BMI (Body Mass Index) Calculator with a Persian GUI interface built using Python's tkinter library.

## Features

- 🖥️ Clean graphical user interface
- 📊 Accurate BMI calculation
- 🎯 BMI category classification
- 🔄 Input reset functionality
- ℹ️ Information dialog with BMI categories
- 🐛 Debug mode for troubleshooting
- ✅ Input validation and error handling

## BMI Categories

| BMI Range | Category |
|-----------|----------|
| < 18.5 | Underweight |
| 18.5 - 24.9 | Normal |
| 25.0 - 29.9 | Overweight |
| ≥ 30.0 | Obesity |

## Requirements

- Python 3.x
- tkinter (usually included with Python)

### Installing tkinter

**On Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install python3-tk
```

**On Fedora:**
```bash
sudo dnf install python3-tkinter
```

**On macOS:**
```bash
brew install python-tk
```

**On Windows:**
tkinter is usually included with Python installation. If not, reinstall Python with tkinter option enabled.

## Usage

### Running the Application

```bash
python3 BMI.py
```

### Debug Mode

To run with debug output for troubleshooting:

```bash
python3 BMI.py --debug
```

Debug mode will print detailed information about:
- Input values
- Calculated BMI
- Error messages
- Application lifecycle events

## How to Use

1. **Enter Height**: Input your height in centimeters (e.g., 175)
2. **Enter Weight**: Input your weight in kilograms (e.g., 70)
3. **Calculate**: Click the "محاسبه کردن" (Calculate) button
4. **View Result**: A popup will show your BMI and category
5. **Reset**: Click "پاکسازی" (Clear) to reset inputs
6. **Info**: Click "اطلاعات" (Information) to view BMI categories

## Input Validation

The application includes robust error handling:
- ✅ Accepts decimal numbers (e.g., 175.5 cm, 70.2 kg)
- ❌ Rejects negative or zero values
- ❌ Rejects non-numeric input
- ❌ Displays clear error messages

## Troubleshooting

### tkinter Module Not Found

If you encounter `ModuleNotFoundError: No module named '_tkinter'`:

1. Install tkinter using the commands in the Requirements section
2. Verify installation:
   ```bash
   python3 -c "import tkinter; print('tkinter installed successfully')"
   ```

### Application Won't Start

1. Ensure you have Python 3.x installed:
   ```bash
   python3 --version
   ```
2. Run in debug mode to see detailed error messages:
   ```bash
   python3 BMI.py --debug
   ```

### GUI Not Displaying

On headless servers or Docker containers without display support:
- The application requires a graphical environment
- Consider using VNC or X11 forwarding for remote access
- Alternatively, run on a system with a display

## Technical Details

### BMI Formula

```
BMI = weight(kg) / (height(m))²
```

Where:
- Weight is in kilograms
- Height is converted from centimeters to meters (divided by 100)

### Bug Fixes in v1.1

1. **Fixed boundary conditions** in BMI categorization:
   - Previously: `bmi > 18.5 and bmi < 24.9` (missed exact values)
   - Now: `bmi <= 24.9` (includes boundary values)

2. **Improved input handling**:
   - Changed from `int()` to `float()` for decimal support
   - Added validation for negative/zero values

3. **Enhanced error handling**:
   - Added try-except blocks
   - Clear error messages for users
   - Debug mode for developers

4. **Better info dialog**:
   - Complete BMI category reference
   - Formatted for readability

## Credits

Designed by: طاها دژبانی (Taha Dezhbani)

## Version History

- **v1.1** (2026-02-04): Added debug mode, fixed bugs, improved error handling
- **v1.0**: Initial release with basic BMI calculation

## License

Open source - feel free to use and modify.
