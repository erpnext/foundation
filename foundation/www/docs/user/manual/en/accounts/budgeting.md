<!-- add-breadcrumbs -->
# Budgeting

In ERPNext, you can set and manage budgets against a cost center or a project. This is useful in controlling your expenses.

For example, if you are doing online sales, you can set a budget for search ads, and configure ERPNext to stop or warn you from over spending beyond the budget set.

Budgets are also great for planning purposes. When you are making plans for the next financial year, you would typically target a revenue based on which you would set your expenses. Setting a budget will ensure that your expenses do not get out of hand, at any point.

### Cost Center

To create new Cost Center, go to:

> Accounts > Budget and Cost Center > Chart of Cost Center > Add New Cost Center

<img class="screenshot" alt="Budget" src="{{docs_base_url}}/assets/img/accounts/budgeting-cost-center.png">

### Project

To create new Project, go to:

> Projects > project > Add New Project

<img class="screenshot" alt="Budget" src="{{docs_base_url}}/assets/img/accounts/new_project.png">


### Setting a budget

#### Step 1: Create a new Budget

To define a Budget, go to:

> Accounts > Budget and Cost Center > Budget > New

#### Step 2: Select Cost Center or Project

In the Budget form, select a Cost Center or a Project. Budgets can be defined against any Cost Center, whether it is a Group / Leaf node in the Chart of Cost Centers.

#### Step 3: Select Account

In the Budgets table, select Income / Expense account for which budget is to be defined.

<img class="screenshot" alt="Budget" src="{{docs_base_url}}/assets/img/accounts/budget-account.png">

#### Step 4: Monthly Distribution

If you have seasonal business, you can also define a Monthly Distribution record, to distribute the budget between months. If you don't set the monthly distribution, ERPNext will calculate the budget on yearly
basis or in equal proportion for every month.

<img class="screenshot" alt="Monthly Distribution" src="{{docs_base_url}}/assets/img/accounts/monthly-budget-distribution.png">

#### Step 5: Control Actions(Alerts)

Control actions can be triggered while material request is being submitted, purchase order is being submitted or while actual expense is being posted(through a journal entry or a purchase invoice).  

There are three types of control actions.

* Stop: This will not allow users to submit the transaction.

* Warn: This will show a warning message but lets the user to submit the transaction.

* Ignore: This will neither prevent the user from submitting transaction nor show an error message.

<img class="screenshot" alt="Control Actions" src="{{docs_base_url}}/assets/img/accounts/control-action.png">

You can set separate action for monthly and annual budgets.

<img class="screenshot" alt="Monthly Distribution" src="{{docs_base_url}}/assets/img/accounts/budget-warning.png">

####Budget Variance Report

At any point of time, user can check Budget Variance Report to analyse the actual expense incurred vs budget allocated against a cost center or a project.

To check Budget Variance report, go to:

Accounts > Budget and Cost Center > Budget Variance Report

<img class="screenshot" alt="Budget Variance Report" src="{{docs_base_url}}/assets/img/accounts/budget-variance-report.png">

<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/wWHkB0jlXNk?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>

{next}
