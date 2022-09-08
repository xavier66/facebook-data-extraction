# Automation tools + IP hiding techniques

In this method, I will write example scripts to extract id, user info, content, date, comments, and replies of posts.

> Demo: https://www.youtube.com/watch?v=Fx0UWOzYsig

**Note**:

-   These scripts just working for **a Facebook page when not sign-in**, not group or any other object.
-   Maybe you will need to edit some of the CSS Selectors in the scripts, as Facebook might have changed them at the time of your use.

## Knowledge

### I. Automation tools

After many research, I think these 3 automation tools would be the wise choices:

-   [Selenium](https://www.selenium.dev): this seems quite slow.
-   [Puppeteer](https://pptr.dev): this can only use on Chrome.
-   [Playwright](https://playwright.dev): this seems to overcome the disadvantages of the 2 above.

You can read the comparisons of the above tools in these link:

-   https://www.bestproxyreviews.com/playwright-vs-puppeteer-vs-selenium
-   https://blog.checklyhq.com/cypress-vs-selenium-vs-playwright-vs-puppeteer-speed-comparison

### II. IP hiding techniques

| Method       | Speed rating | Cost         | Common risk                             | General Evaluation |
| ------------ | :----------: | ------------ | --------------------------------------- | ------------------ |
| VPN service  |     `2`      | Usually paid | Some free providers might not be secure | Best way           |
| Tor browser  |     `4`      | Free         | Can be tracked by some rogue nodes      | Slowest choice     |
| Proxy server |     `3`      | Usually free | Data routing not private as VPNs        | Riskiest method    |
| Public WiFi  |     `1`      | Free         | Some might not be safe                  | Long distance way  |

➔ Learn more about general information of above methods from this [site](https://whatismyipaddress.com/hide-ip).

**IMPORTANT**: Nothing above is absolutely safe and secure. _Carefulness is never excessive_. You will need to do further research about them if you want more secure to your data & privacy.

## Overview the scripts

### I. Features

1.  Getting information of posts.
2.  Filtering comments.
3.  Checking redirect.
4.  Can be run with Incognito window.
5.  Simplifying browser to minimize time complexity.
6.  Delay with random intervals every _loading more_ times to simulate human behavior.
7.  Not required sign-in to **prevent Checkpoint**.
8.  Hiding IP address to **prevent from banning** by:
    -   Collecting proxies and filtering the slowest ones from:
        -   http://proxyfor.eu/geo.php
        -   http://free-proxy-list.net
        -   http://rebro.weebly.com/proxy-list.html
        -   http://www.samair.ru/proxy/time-01.htm
        -   https://www.sslproxies.org
    -   [Tor Relays](https://github.com/18520339/facebook-crawling/tree/master/2%20-%20Automation%20tools%20with%20IP%20hiding%20techniques/tor) which used in [Tor Browser](https://www.torproject.org/), a network is comprised of thousands of volunteer-run servers.

### II. Weaknesses

-   Unable to detect some failed responses. Example: **Rate limit exceeded** (Facebook prevents from loading more).

    ![](https://github.com/18520339/facebook-crawling/blob/master/2%20-%20Automation%20tools%20with%20IP%20hiding%20techniques/img/rate_limit_exceeded.png?raw=true)

    ➔ Have to run with `HEADLESS = False` to detect manually.

-   Quite slow when running with a large number of _loading more_ or when using [IP hiding techniques](#ii-ip-hiding-techniques).

### III. Result

-   Each post will be separated [line by line](https://raw.githubusercontent.com/18520339/facebook-crawling/master/2%20-%20Automation%20tools%20with%20IP%20hiding%20techniques/data/KTXDHQGConfessions-inline.json).
-   Most of my successful tests were on **Firefox** with [HTTP Request Randomizer](https://github.com/pgaref/HTTP_Request_Randomizer) proxy server.
-   My latest run on **Firefox** with **Incognito** windows using [HTTP Request Randomizer](https://github.com/pgaref/HTTP_Request_Randomizer):

    ![](https://github.com/18520339/facebook-crawling/blob/master/2%20-%20Automation%20tools%20with%20IP%20hiding%20techniques/img/result.png?raw=true)

<details>
    <summary>
        <b>Example data fields for a post</b>
    </summary><br/>
    
```json
{
    "url": "https://www.facebook.com/KTXDHQGConfessions/videos/352525915858361/",
    "id": "352525915858361",
    "utime": "1603770573",
    "text": "Diễn tập PCCC tại KTX khu B tòa E1. ----------- #ktx_cfs Nguồn : Trường Vũ",
    "reactions": ["308 Like", "119 Haha", "28 Wow"],
    "total_shares": "26 Shares",
    "total_cmts": "169 Comments",
    "crawled_cmts": [
        {
            "id": "Y29tbWVudDozNDM0NDI0OTk5OTcxMDgyXzM0MzQ0MzIyMTY2MzcwMjc%3D",
            "utime": "1603770714",
            "user_url": "https://www.facebook.com/KTXDHQGConfessions/",
            "user_id": "KTXDHQGConfessions",
            "user_name": "KTX ĐHQG Confessions",
            "text": "Toà t á bây :) #Lép",
            "replies": [
                {
                    "id": "Y29tbWVudDozNDM0NDI0OTk5OTcxMDgyXzM0MzQ0OTc5MDk5NjM3OTE%3D",
                    "utime": "1603772990",
                    "user_url": "https://www.facebook.com/KTXDHQGConfessions/",
                    "user_id": "KTXDHQGConfessions",
                    "user_name": "KTX ĐHQG Confessions",
                    "text": "Nguyễn Hoàng Đạt thật đáng tự hào :) #Lép"
                }
            ]
        }
    ]
}
```
</details>

## Usage

### I. Install libraries

    pip install -r requirements.txt

-   [Helium](https://github.com/mherrmann/selenium-python-helium): a wrapper around [Selenium](https://selenium-python.readthedocs.io/) with more high-level API for web automation.
-   [HTTP Request Randomizer](https://github.com/pgaref/HTTP_Request_Randomizer): used for collecting free proxies.

### II. Customize parameters in [crawler.py](https://github.com/18520339/facebook-crawling/blob/master/2%20-%20Automation%20tools%20with%20IP%20hiding%20techniques/crawler.py)

1.  **Running browser**:

    -   **PAGE_URL**: url of Facebook page.
    -   **TOR_PATH**: use proxy with Tor for `WINDOWS` / `MAC` / `LINUX` / `NONE`:
    -   **BROWSER_OPTIONS**: run scripts using `CHROME` / `FIREFOX`.
    -   **PRIVATE**: run with private mode or not:
        -   Prevent from **Selenium** detection ➔ **navigator.driver** must be _undefined_ (check in Dev Tools).
        -   Start browser with **Incognito** / **Private Window**.
    -   **USE_PROXY**: run with proxy or not. If **True** ➔ check:
        -   IF **TOR_PATH** &ne; `NONE` ➔ Use **Tor's SOCKS** proxy server.
        -   ELSE ➔ Randomize proxies with [HTTP Request Randomizer](https://github.com/pgaref/HTTP_Request_Randomizer).
    -   **HEADLESS**: run with headless browser or not.
    -   **SPEED_UP**: simplify browser for minimizing loading time or not. If **True** ➔ use following settings:

        -   With **Chrome** :

        ```python
        # Disable loading image, CSS, ...
        browser_options.add_experimental_option('prefs', {
            "profile.managed_default_content_settings.images": 2,
            "profile.managed_default_content_settings.stylesheets": 2,
            "profile.managed_default_content_settings.cookies": 2,
            "profile.managed_default_content_settings.geolocation": 2,
            "profile.managed_default_content_settings.media_stream": 2,
            "profile.managed_default_content_settings.plugins": 1,
            "profile.default_content_setting_values.notifications": 2,
        })
        ```

        -   With **Firefox** :

        ```python
        # Disable loading image, CSS, Flash
        browser_options.set_preference('permissions.default.image', 2)
        browser_options.set_preference('permissions.default.stylesheet', 2)
        browser_options.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
        ```

2.  **Loading page**:

    -   **SCROLL_DOWN**: number of times to scroll for **view more posts**.
    -   **FILTER_CMTS_BY**: filter comments by `MOST_RELEVANT` / `NEWEST` / `ALL_COMMENTS`.
        ![](https://github.com/18520339/facebook-crawling/blob/master/2%20-%20Automation%20tools%20with%20IP%20hiding%20techniques/img/filter.png?raw=true)
    -   **VIEW_MORE_CMTS**: number of times to click **view more comments**.
    -   **VIEW_MORE_REPLIES**: number of times to click **view more replies**.

### III. Start running

    python crawler.py

-   Run at sign out state, cause some CSS Selectors will be different as sign in.
-   With some proxies, it might be quite slow or required to sign in (redirected).
-   **To achieve higher speed**:
    -   If this is first time using these scripts, you can **run without tor & proxies** until Facebook requires to sign in.
    -   Use some popular **VPN services** (also **run without tor & proxies**): [NordVPN](https://nordvpn.com), [ExpressVPN](https://www.expressvpn.com), ...

## Test proxy server

1. With [HTTP Request Randomizer](https://github.com/pgaref/HTTP_Request_Randomizer):

```python
from browser import *
page_url = 'http://check.torproject.org'
proxy_server = random.choice(proxies).get_address()
browser_options = BROWSER_OPTIONS.FIREFOX

setup_free_proxy(page_url, proxy_server, browser_options)
# kill_browser()
```

2. With [Tor Relays](https://github.com/18520339/facebook-crawling/tree/master/2%20-%20Automation%20tools%20with%20IP%20hiding%20techniques/tor):

```python
from browser import *
page_url = 'http://check.torproject.org'
tor_path = TOR_PATH.WINDOWS
browser_options = BROWSER_OPTIONS.FIREFOX

setup_tor_proxy(page_url, tor_path, browser_options)
# kill_browser()
```

![](https://github.com/18520339/facebook-crawling/blob/master/2%20-%20Automation%20tools%20with%20IP%20hiding%20techniques/img/proxy.png?raw=true)
