# emis-alert

This project is a Python script and a systemd service that provides an alert service for monitoring changes in the `emis.freeuni.edu.ge` website. It periodically checks the website for updates and sends notifications when changes are detected.

## Installation

1. Clone the repository
2. Install the required dependencies:

   ```shell
   pip install requests beautifulsoup4
   ```
3. Install [Messer](https://github.com/mjkaufer/Messer)

## Usage

1. Create a file named `name` in the project directory and write your name in it. This name will be used for sending notifications.

2. Run the script with the PHP session ID as a command-line argument:

   ```shell
   python emis_alert.py <PHPSESSID>
   ```

   For example:

   ```shell
   python emis_alert.py abcdef1234567890
   ```

3. The script will start monitoring the EMIS website for changes. It will check for updates every 5 seconds.

## Disclaimer

This project is abandoned, archived and further development is not planned. Messaging with "Messer" never worked well and almost always resulted in the account getting suspended. This project is provided as-is without any warranty, use at your own risk.

## License

This project is licensed under the [MIT License](LICENSE).
