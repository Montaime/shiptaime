# shiptaime
Automation of shipping &amp; handling using Bandcamp's Merch Fullfillment API &amp; Pirate Ship

![shiptaime_cube](https://user-images.githubusercontent.com/71521969/149567441-4a925ddd-ffea-452a-bfab-459847bab063.png)

***
```
Copyright (c) 2022 Montaime LLC

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.

Montaime uses Bandcamp for merch handling & processing. Bandcamp's API is 
currently being implemented into shiptaime. In order to use Bandcamp API
features, you must directly contact Bandcamp's support to ask for permission.

Montaime LLC does not offer support on how to gain access to Bandcamp's dev
tools or API. Montaime LLC is not affilited with Bandcamp, Inc. We just love
their platform ;)
```
***

### How Montaime does shipping & handling
Montaime uses Pirate Ship, a free shipping & handling software to ship merchandise such as vinyl records, cassettes
and more. However, **Pirate Ship does not feature direct integration with Bandcamp**, the platform we use to sell 
merchandise.

Bandcamp provides customer information via `.csv` files, which we convert to `.xlsx` spreadsheets. Pirate Ship provides
a method of importing these spreadsheets, allowing Montaime to quickly bulk purchase domestic & international shipping labels.

### The big issue
Pirate Ship only provides a basic email service to let customers know a shipment's status, which is handled via a basic
email service. However, it lacks flexibility to set custom messages for customers. Additionally, customers are more likely to click on
Bandcamp order status emails- which can **only be updated Bandcamp's own website.**

Due to the lack of integration from Pirate Ship's platform to Bandcamp, the initial solution was to copy/paste tracking 
information alongside a brief message to each customer. As Montaime's customer base has expanded to hundreds of people, 
**this approach is becoming increasingly difficult (and extremely time consuming).**

### Setup & instructions 
This software uses Pandas, an Python library to parse Pirate Ship formatted `.xlsx` spreadsheets. Please
overview the `requirements.txt` file for additional requirements information.

To use shiptaime, run the `parse.py` script via command-line.

You will be prompted for a valid path of a Excel spreadsheet via the command line. Not properly specifying the spreadsheet
will result in an `Invalid spreadsheet!` error message, followed by program termination.

If a valid spreasheet is detected, shiptaime parses the Customer name, email, tracking number utilized by Montaime, and determines the appropriate shipping service
based on a several characteristics determined by the tracking number provided.

### Important functions & sorting capabilities
`AHOY_check()` checks several characteristics of a tracking number provided.
If the tracking number starts with the characters "AHOY", it is sorted under the Simple Export Rate service. If this is false, the function checks whether the tracking number is entirely numeric (no symbols/alphabetic characters). If this is true, it is sorted as a USPS Domestic shipment. If the two above conditions are false, the tracking number is sorted as a USPS International shipment.

Since 2021, the majority of international shipments fulfilled by Pirate Ship is done via the "Simple Export Rate" service, provided by Asendia (a third party shipping courier). Therefore, the use of a custom tracking number is used, with a custom tracking URL provided after the shipping label is purchased. shiptaime takes this custom URL and parses it, so the URL can be automatically be provided to a customer.

Currently, shiptaime writes associated tracking information into a `.txt` file which clearly delimits the customer name,
email and shipping message provided to the customer. This implementation has still sped up shipping updates via Bandcamp by 80-90%. 

### Other experiments 
- Attempting to directly request a Pirate Ship spreadsheet from an account didn't based on a shipping ID did NOT work- 
and is apparently prohibited under Pirate Ship's user license agreement. Due to this, crawling attempts were stopped. 
The software is intented to function only with Pirate Ship spreadsheets that are directly requested via their user UI, and Pirate Ship has no intentions
currently of opening their API to users.
- Integration via the Bandcamp API is the next important step in order to automatically update tracking statuses for customers. There still isn't a solution on how to handle multiple shipmentsfrom a user, and how to differentiate between orders from multiple users. Likely, this will be an edge case that must be tested.
