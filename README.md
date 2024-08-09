# Insecure Headers Testing

This project is a Python script designed to test websites for the presence of various HTTP security headers. By checking these headers, you can determine whether a site is vulnerable to certain types of attacks or is configured securely.

## Features

- **X-XSS-Protection:** Checks if the `X-XSS-Protection` header is properly set to prevent cross-site scripting (XSS) attacks.
- **X-Content-Type-Options:** Verifies if the `X-Content-Type-Options` header is set to `nosniff`, preventing browsers from MIME-type sniffing.
- **Strict-Transport-Security (HSTS):** Ensures the presence of the HSTS header, which protects against man-in-the-middle (MITM) attacks by enforcing secure (HTTPS) connections.
- **Content-Security-Policy (CSP):** Checks for the `Content-Security-Policy` header to mitigate a wide range of attacks, including XSS and data injection.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/arifbinekram/Insecure-Headers-Testing.git
   cd Insecure-Headers-Testing
   ```

2. **Install the required Python packages:**

   The script requires Python 3 and the `requests` library. Install the required package using pip:

   ```bash
   pip3 install requests
   ```

## Usage

1. **Prepare your URLs:**

   Create a file named `urls.txt` in the root directory of the project. List all the URLs you want to test, one per line. For example:

   ```
   https://www.example.com
   https://www.anotherexample.com
   ```

2. **Run the script:**

   Execute the script using Python 3:

   ```bash
   python3 header.py
   ```

   The script will read the URLs from `urls.txt`, check each URL for security headers, and output a report for each URL.

## Output

The script outputs information about the security headers for each URL, indicating whether:

- `X-XSS-Protection` is properly set.
- `X-Content-Type-Options` is configured as `nosniff`.
- `Strict-Transport-Security` (HSTS) is present.
- `Content-Security-Policy` (CSP) is defined.


## Contributions

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to discuss potential improvements or features.

## Acknowledgments

- This script is inspired by the need to quickly assess web applications for basic security header configurations.
- Special thanks to the open-source community for their continuous support and contributions.

---

For more information, visit the [project repository](https://github.com/arifbinekram/Insecure-Headers-Testing).
```

This README provides a comprehensive overview of the project's purpose, features, installation instructions, usage guidelines, and other important details. Adjust any sections as needed to fit additional project specifics or updates.
