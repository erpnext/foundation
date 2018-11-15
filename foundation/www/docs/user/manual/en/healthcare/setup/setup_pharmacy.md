<!-- add-breadcrumbs -->
# Setting Up Pharmacy
ERPNext Healthcare do not have a Pharmacy module as such. However, [ERPNext Stock](/docs/user/manual/en/stock), [Buying](/docs/user/manual/en/buying) and [Accounts](/docs/user/manual/en/accounts) Module will do all that's needed to seamlessly manage your Pharmacy Stock as well as other supplies, their billing and purchases.

You can also consider creating multiple [POS Profiles](/docs/user/manual/en/setting-up/pos-setting) for each Pharmacy user. ERPNext Stock module features like [Items](/docs/user/manual/en/stock/item) with Reorder Levels and [Auto Reordering](/docs/user/manual/en/stock/item/reorder), [Batch Number and Expiry Dates](/docs/user/manual/en/stock/batch) etc. will be worth looking at.

ERPNext Healthcare adds a few custom fields to `Item` document so that you can effectively configure medicines. Also read [Healthcare Settings](/docs/user/manual/en/healthcare/setup/healthcare_settings) for setting up default Items, Accounts etc.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/items_custom_fields.png">

>Note that these fields are made available only if your setup has Healthcare domain enabled.

Furthermore, all the three modules comes with exhaustive reporting and you can also configure auto email to have reports emailed automatically to you.

{next}
