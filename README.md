# Baby's First Weather App

## Features

- Fetches current weather data for any location.
- Displays latitude longitude coordinates, temperature, wind speed, and weather conditions.
- CLI based interface
- Lightweight and easy to set up.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Scaarliege/Babys-First-Weather-App.git
    cd Babys-First-Weather-App
    ```

2. Install the required dependencies:

    ```bash
    pip install requests
    ```
    ```bash
    pip install geocoder
    ```
   
## Usage

1. Run the application:
   
    ```bash
    python main.py
    ```

2. Follow the prompts to enter the location for which you want to fetch the weather data.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Nominatim](https://nominatim.org/) for providing the lat-long coordinates to City conversions.

- [Open-Meteo](https://open-meteo.com/) for providing the weather services.
