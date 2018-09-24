A Finance Book is a book against which all the accounting entries are booked. You can have multiple finance books, for example one book for tax authorities and another for stockholders.

This is useful if you have to report depreciation and other values in different ways based on regulatory requirements. You can also use this to post alternate balance sheets for your internal reporting.

In ERPNext, Finance Book is not a mandatory setup. But if you choose to create multiple finance books, then you can make entries against a specific finance book by selecting that book in Journal Entry. If a Finance Book field is blank in Journal Entry that means the entry will be available in all finance books.

Many a times, for fixed asset depreciation, company use different depreciation method (Straight Line / Written Down Value / Double Declining Balance) for different finance book. In ERPNext, you can setup different depreciation schedule for each finance book and auto depreciations will booked against that finance book only.

<img class="screenshot" alt="Finance Book" src="{{docs_base_url}}/assets/img/accounts/finance-book.png">