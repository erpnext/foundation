<!-- add-breadcrumbs -->
# Email Domains

You can configure your Email Domain in ERPNext for easy setup of all Email Accounts. You can find domain settings under Setup-->Email Domain.

> **What is my Email Domain?:** You might have purchased Email service from your internet service provider or your IT service provider. For example, if you access your business mailbox with URL like http://mail.mybusiness.com, then mybusiness.com is your email domain. And without setting up email domain correctly, your ERPNext instance might not be able to receive mails even though outgoing mails might work. You may be using commercial mail services like gmail or yahoo. In this case google.com or yahoo.com is your email domain.

### Default Email Domain

ERPNext creates a template email domain using example.com for your reference. You can add your domain by clicking on the new button.

<img class="screenshot" alt="Email Domain" src="{{docs_base_url}}/assets/img/setup/email/email-domain.png">

### Example Email Address

Example Email Address is where you enter your business email address, For example, if your email ID is myname@mybusinessdomain.com you should enter this here.

### Email Server

This is the internet address or URL of your mail server or the email service that you have purchased. For Example it may be mail.mybusiness.com or imap.mybusiness.com. 

### USE IMAP

If your Email server uses IMAP service for the incoming mails keep this checked. Otherwise leave this unchecked.

### USE SSL

If your mail server uses SSL (Secure Socket Layer) communication leave this checked. You may have purchased SSL certificate from your IT service provider for the SSL setup.

### Attachment Limit (MB)

If you want to limit the size of file attachments for emails sent from within ERPNext, you can set that up here. You can enter the size of attachments in MB.

### SMTP Server

This is the address of service of outgoing mails of your email server.

### Use TLS

Set this up if your SMTP service is setup with TLS.

### Default port

SMTP service is usually set on port 25. If your email serer is setup on a separate port number you can set that up here.

