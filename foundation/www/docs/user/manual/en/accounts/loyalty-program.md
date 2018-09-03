<!-- add-breadcrumbs -->
# Loyalty Program


### What is a Loyalty Program?

A customer loyalty program is a structured and long-term marketing effort which provides incentives to repeat customers who demonstrate loyal buying behavior. Successful programs are designed to motivate customers in a business's target market to return often, make frequent purchases, and shun competitors.

<br>
To create a **Loyalty Program** go to:

> Accounts > Billing > Loyalty Program > New

<img class="screenshot" alt="Loyalty Program" src="{{docs_base_url}}/assets/img/accounts/loyalty-program.png">

In a Loyalty Program, you must select.

  * Type of Program from the drop down.
  * From Date - to provide when to start considering this Program.
  * End Date - to provide till when should this Program's effect be considered.
  * Auto Opt-in to automatically select a Program when creating a new Customer.
  * Add rows for the Collection Tier. In each row, you must specify: 
    * Tier name to be assigned to a Customer based on his eligibility.
	* Collection Factor - how much of an amount constitues 1 loyalty point.
	* Minimum Spent - minimum transaction amount to be eligible for this tier.

* * *

## Loyalty Point Entry
<br>
**Loyalty Point Entry** acts as a log to give an overview about which Customer earned how many points across which Invoice. It holds the data Invoice and Customer.

<img class="screenshot" alt="Loyalty Program 3" src="{{docs_base_url}}/assets/img/accounts/loyalty-program-3.png">

* * *

## Customer
<br>
**Loyalty Program** section in Customer master.

<img class="screenshot" alt="Loyalty Program 1" src="{{docs_base_url}}/assets/img/accounts/loyalty-program-1.png">

<br>
**Loyalty Point** earned can be viewed in Customer's dashboard.

<img class="screenshot" alt="Loyalty Program 2" src="{{docs_base_url}}/assets/img/accounts/loyalty-program-2.png">

* * *

# How it works ?

### Earning Points
* Firstly, a **Loyalty Program** needs to be created (as shown in the first screenshot).
* Assign this **Loyalty Program** to a **Customer**.
* Goto `Sales Invoice > New` and create an invoice for the **Customer** to whom you have assigned **Loyalty Program**.
* For this example, an invoice is created with a grand total of `10000 INR` and according to the **Loyalty Program** for a minimum spent of `10000` INR, the Silver Tier collection factor will be eligible and for each `1000` INR spent, the **Customer** will receive 1 point (hence the total point earned on this transaction is 10).
* Upon submission of the invoice, **Loyalty Point Entry** will be created for this invoice (as shown above under Loyalty Program Entry section).
* In the **Loyalty Program** upon minimum spent of `19000`, Gold Tier would be eligible. So, if we were to duplicate our current invoice and submit it, the **Customer** will be automatically upgraded to Gold tier as his total expenditure under this current **Loyalty Program** has exceeded the minimum spent value for Gold tier collection factor (as his last invoice was `10000` INR and duplicated from that gives another invoice of `10000` INR, hence his total expenditure becomes `20000` INR).

> Note: The minimum spent in Loyalty Program does not mean a minimum value for a single invoice. Rather it means the sum of amount of invoices for that customer under a particular LOyalty Program scheme.

### Redeeming Points
* Continuing from the above example where we have created 1 invoice and earned 10 points over it, we create another invoice by duplicating the first, and under the collapsible section for **Loyalty Program**, we check the checkbox for `Redeem Loyalty Points`.
* The fields for `Loyalty Point`, `Redemption Account` and `Redemption Cost Center` will become visible under this section. The account and cost center will be fetched from the **Loyalty Program** assigned to the **Customer**.
* Since we have earned 10 points, we can use as many of them as we want. If we try to use more than what we have an error will be thrown.
* For this example, we'll use all 10 points to be redeemed. Doing so will enable another field which will display the amount calculated using ( loyalty point * convertion factor ). So basically, `10` INR will be lessened from our outstanding amount.
* When submitted, 2 **Loyalty Point Entry** will be created. One for redeemed, which will be a negative value and one for the current invoice (as the amount is still eligible under a tier).

> Note: For an invoice on which points have been earned, if a return invoice is created, it will delete the original Loyalty Point Entry and create a new one after subtracting the original amount with the returned amount. Also, when cancelling an invoice, its subsequent Loyalty Point Entry will also be deleted.

{next}