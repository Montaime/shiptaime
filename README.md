# shiptaime
Automation of shipping &amp; handling using Bandcamp's Merch Fullfillment API &amp; Pirate Ship

Montaime uses Bandcamp's API for merch handling, which is currently being implemented into shiptaime. 

Anyone attempting to use shiptaime does so at their own risk- there is no warranty or support associated with this 
release.

### How Montaime does shipping & handling
Montaime uses Pirate Ship, a free shipping & handling software to ship merchandise such as vinyl records, cassette tapes
and more. However, **Pirate Ship does not feature direct integration with Bandcamp**, the platform we use to sell 
merchandise.

Bandcamp provides customer order information to us via `.csv` files, which we can easily convert to `.xlsx` spreadsheets. 

Luckily, Pirate Ship provides a way to import these spreadsheets. You import an `.xlsx`, allowing one to
quickly bulk-purchase hundreds of domestic and international shipping labels. You can provide package weight, customs
information, IOSS numbers, harmonization codes and more.

### The big issue
Pirate Ship does not provide any flexible tools to inform customers that their order is on the way. They provide a basic
email service if an email is associated to a customer's order, which informs them that their order is being processed. 
However, our customers directly watch out for Bandcamp status emails regarding their order- which can **only be updated 
Bandcamp's own website.**

Due to the lack of integration from Pirate Ship's platform to Bandcamp, the initial solution was to copy/paste tracking 
information alongside a brief message to each customer. As Montaime's customer base has expanded to hundreds of people, 
**this approach is becoming increasingly difficult (and extremely time consuming).**

### Setup & instructions 
This application uses Pandas, an imported Python library to parse Pirate Ship formatted `.xlsx` spreadsheets. Please
overview the `requirements.txt` file for additional requirements information.

The user is prompted for a valid path of a Excel spreadsheet via the command line. Not properly specifying the spreadsheet
will result in an `Invalid spreadsheet!` error message, followed by program termination.

If a valid spreasheet is detected, shiptaime parses the Customer name, email, tracking number utilized by Montaime, and determines the appropriate shipping service
based on a few characteristics determined by the tracking number provided.

The parsing function `AHOY_check()` checks whether a tracking number starts with the characters "AHOY". If it does,
we treat that tracking number under the "Simple Export Rate" service, which is fulfilled by the third party Asendia. 
Tracking numbers with this identifier are treated differently, and a tracking URL is parsed which is 
provided to the customer.

Otherwise, `AHOY_check()` checks whether a tracking number is entirely numeric (no symbols or alphabetic characters). If
so, this tracking number is treated as a USPS domestic tracking number.

If `AHOY_check()` checks a tracking number which is not a part of the Simple Export Rate service, and is not entirely
numeric, it's treated as a USPS international tracking number.

Currently, shiptaime writes associated tracking information into a `.txt` file which clearly delimits the customer name,
email and shipping message provided to the customer.

Currently, this method has sped up shipping updates via Bandcamp by 80-90%. 
Work is currently being done to integrate this parsed information with the Bandcamp API, to instantaneously update 
tracking status for customers.

### Other experiments 
- Attempting to directly request a Pirate Ship spreadsheet from an account didn't based on a shipping ID did NOT work- 
and is apparently prohibited under Pirate Ship's user license agreement. Due to this, crawling attempts were stopped. 
The software is intented to function only with Pirate Ship spreadsheets that are directly requested via their user UI, and Pirate Ship has no intentions
currently of opening their API to users.
- Integration via the Bandcamp API is the next important step- there still isn't a solution on how to handle multiple shipments
from a user, and how to differentiate between orders from multiple users. Likely, this will be an edge case that must be tested.