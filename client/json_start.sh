#! /bin/bash

java -Dwebdriver.chrome.driver="../driver/chromedriver" -jar ../lib/selenium-server-standalone.jar -role node -nodeConfig webdriver.json
