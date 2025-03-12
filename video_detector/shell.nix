{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "assembleia-scribe-shell";
  buildInputs = [
    pkgs.python39Full
    pkgs.python39Packages.selenium
    pkgs.chromium
    pkgs.chromedriver
  ];

  # Set environment variables for Selenium to locate Chromium.
  shellHook = ''
    export CHROME_BIN=${pkgs.chromium}/bin/chromium
    echo "Shell ready: Python $(python --version), Chromium set to $CHROME_BIN"
  '';
}
