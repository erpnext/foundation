# Job Card

A Job Card is created from the Work Order and given to each of the workstation in the manufacturing floor to start the production of an item with a certain quantity in each of the operations defined in the Work Order.

The Job Card extends the functionality of the Work Order in the manufacturing process by adding/defining phase of operations in work orders and assigning each operations into their respective workstation.

Job Card allows each operation's workstation to issue a “Material Request” and “Stock Transfer to Manufacture” for raw material required against a “Job Card” order assigned to them.

Job Card completion will change the production status in Work Order, we can track completion of production progress for each of the operations defined in the work order.

> Manufacturing > Work Order > Create Job Card

### Job Card creation based on BOM

In the Work Order, the Operations and Workstations are fetched from the BOM of an Item. Hence, you should ensure that Routing (master of Operations and Production) is configured in the BOM. Here are the steps for the same.

- Define the Item BOM for production, select “With Operations” on the checklist.

<img class="screenshot" alt="Create Shareholder" src="/docs/assets/img/manufacturing/bom-operrations-job-card.png">

- Define the production flow by selecting operations in BOM.

<img class="screenshot" alt="Create Shareholder" src="/docs/assets/img/manufacturing/bom-operation-rounting.png">

- Select Item required for production, assign each of the Item into Operations.

<img class="screenshot" alt="Create Shareholder" src="/docs/assets/img/manufacturing/bom-item-job-card.png">

> You can select “Transfer Material Against Job Card” to transfer raw material for production based on the Job Card, and not by Work Order.

Define “Operations” cycle/flow involved in the Item
Select the Item required and assign material to operations for manufacturing.

<img class="screenshot" alt="Create Shareholder" src="/docs/assets/img/manufacturing/bom-operation-rounting.png">

You can select “Transfer Material Against Job Card” on the Bill of Material to transfer Material for Production based on Job Card.

### Routing in Work Order

Job Card will be created upon submission of the Work Order based on the Operations defined in the Bill of Material. Each Job Card represents job order for each Workstations on the manufacturing floor.

#### Select Work Order with Item to Manufacture

In the Work Order, define if you want to transfer material against a Job Order or no.

<img class="screenshot" alt="Create Shareholder" src="/docs/assets/img/manufacturing/work-order-transfer-against-job-card.png">

#### Job Card Creation

On submission of Work Order, Job Cards will be auto-created based on the values in the Routing table.

<img class="screenshot" alt="Create Shareholder" src="/docs/assets/img/manufacturing/work-order-job-card-creation.png">

### Job Card

Each Job Card created will have Workstation & Operations assigned. Raw material required from each source warehouse will be calculated based on quantity required for production.

Employee assignment and timing detail will also be defined in Job Card.

<img class="screenshot" alt="Create Shareholder" src="/docs/assets/img/manufacturing/job-card-form.png">

#### Material Request against Job Card

A Material Request will be raised from the Job Card as a basis/order to prepare raw-material required for manufacturing process. The Material Request raised will have its reference to the original Job Card number.

<img class="screenshot" alt="Create Shareholder" src="/docs/assets/img/manufacturing/material-request-against-job-card.png">

Track the Manufacturing Progress in The Work Order by The Completion of Each Operations defined in Work Order.

Job Card completion allow us to track the manufacturing progress inside the Work Order by looking of the completion of each Operations that are related in the Work Order.

<img class="screenshot" alt="Create Shareholder" src="/docs/assets/img/manufacturing/work-order-job-card-completion.png">

