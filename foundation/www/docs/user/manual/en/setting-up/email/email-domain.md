<!-- add-breadcrumbs -->
# Email Domains

You can configure your Email Domain in ERPNext for easy setup of all Email Accounts in ERPNext. You can find domain settings under Setup-->Email Domain.

> **What is my Email Domain?:** You might have purchased Email service from your internet service provider or your IT service provider. For example : If you access your business mailbox with URL like http://mail.mybusiness.com, then mybusiness.com is your email domain. And without setting up email domain correctly, your ERPNext instance might not be able to receive mails even though outgoing mails might work. You may be using commercial mail services like gmail or yahoo. In this case google.com or yahoo.com is your email domain.

<img class="screenshot" alt="Email Domain" src="{{docs_base_url}}/assets/img/setup/email/email-domain.png">

### Default Email Domain

ERPNext creates a template for an example.com email domain.

### Example Email Address

Example Email Address is where you enter your business email address, For example : if your email ID is myname@mybusinessdomain.com enter this here.

### Email Server

This is the internet address or URL of the mail service you have purchased. For Example it may be mail.mybusiness.com or imap.mybusiness.com.

### USE IMAP

If your Mail server uses IMAP service for the incoming mails keep this checked. Otherwise leave this unchecked.
If you want to enable incoming mails within ERPNext Leave this checked 

### USE SSL

If your mail server uses SSL communication leave this checked. 

###Attachment Limit (MB)

If you want to limit the file attachments size to a particular limit in MB for attachments to be a sent via email from ERPNext, You can set that up here.

