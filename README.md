## Table of Contents
  - [Introduction](#introduction)
  - [Why do you Need this App in ERPNext](#why-do-you-need-this-app-in-erpnext)
  - [How to use EMD Management in ERPNext](#how-to-use-emd-management-in-erpnext)
  
  ## Introduction:
  Earnest Money Deposit (EMD) is a sum of money required from bidders as a commitment to participate seriously. It serves as financial assurance and is typically a percentage of the bid amount or a fixed amount. The EMD is held by the government agency or organization conducting the bidding/auction. If the bidder wins but fails to fulfil contractual obligations, the EMD may be forfeited. Understanding EMD requirements is crucial for bidders.
  
[![PNG - 5  How to Manage EMD in ERPNext](https://user-images.githubusercontent.com/18363620/233313402-17d55d15-0183-406f-b40e-ebd55f5699c3.png)](https://youtu.be/oArobHyygSQ)

  ## Why do you Need this App in ERPNext:
   1. Streamlined EMD Management: An EMD app in ERPNext can help you centralize and automate the management of EMDs, making it easier to track, record, and manage EMD transactions in a systematic manner.
   2. Enhanced Financial Control: The EMD app can provide financial control features, such as setting EMD amounts, due dates, refund policies and other charges ensuring that your EMD processes are aligned with your business policies and requirements.
   3. Real-time EMD Status: The EMD app can provide real-time visibility into the status of EMD transactions, including pending EMDs, refunded EMDs, and forfeited EMDs, helping you to monitor and track the EMD status for each transaction.
   4. Send Automated Reminders: EMDs are also type of receivables from customer after maturity date. They system can send automated reminders to customers for follow up for refund of EMDs.
   5. EMD Return and interest management: When EMD are received back with some interest the user can do return entry mentioning interest amount and interest account. System will automatically create respective JV and mark EMD as returned.

 Having an EMD app in ERPNext can provide you with a streamlined solution for efficient and compliant EMD management, aligned with your organization's specific needs and workflows.
 
 ## How to use EMD Management in ERPNext:
  **`At Time of Giving EMD`**:
  * Fill out EMD form with the details such as Customer, Due Date, Deposit Account, Bank Account, Tender Name, Tender No, Amount, Extra Charges, Payment Mode, Reference Number etc. and submit the entry. 
  * On submission the system will create an EMD Journal Entry marking expense for charges and create receivable from customer. 
  * This will also mark EMD status as Paid.

  ![EMD Paid-26-36](https://user-images.githubusercontent.com/18363620/233315309-290c26b3-83a6-450b-99b1-fe8c2b99d395.gif)

  **`When EMD is Due`**:
  * System will check if any EMD has not been received after due date, it will mark the EMD status Due.
If you wish to send reminder for repayment to customer, you can click checkbox “Send Weekly Reminder”. It will make reminder setup section visible.
  * The contact person email address will auto populate in Recipient email. You can add anymore persons in recipient or in CC To field. EMD Reminder email template will auto populate. You can change the text below as per your requirements.
System will send weekly reminders with selected text till the time EMD is not returned.

![EMD Due-52-62](https://user-images.githubusercontent.com/18363620/233315481-005534c0-05df-481a-b057-5a1a05356fb3.gif)


  **`When EMD is Returned`**:
  * Open the EMD which is refunded from customer, and click on check box returned. 
  * Fill Interest amount, account to credit interest and bank account where funds are received in return section.  
  * On update system will pass journal entry for the return and mark the EMD status as refunded.

![EMD Returned-90-100](https://user-images.githubusercontent.com/18363620/233315588-7c33dcb5-7c68-44ff-a3ca-56b9e4c619bc.gif)

   **`If EMD Forfeited`**:
   * If for any reason EMD is forfeited, and you are not expecting is back, you can click on checkbox forfeited. 
   * Select the write off account and system will pass Journal Entry for the writing off EMD from balance sheet and mark EMD status as forfeited.

![EMD Forfieted-115-125](https://user-images.githubusercontent.com/18363620/233315656-9e4b95b6-f7a9-4b5a-bcff-70f069e76137.gif)

## Documentation

Complete documentation for EMD Management [here](https://finbyz.tech/emd-management-erpnext)

## License

GNU GPL V3. (See [license.txt](https://github.com/finbyz/emd_management/blob/main/license.txt) for more information).

The EMD Management code is licensed as GNU General Public License (v3) and the copyright is owned by FinByz Tech Pvt Ltd.

