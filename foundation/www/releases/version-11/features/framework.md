# Framework Enhancements

Frappe Framework sits at the foundation of ERPNext and is the core technology that drives this application. There have been huge improvements on the Framework side as we make ERPNext even more ready for the next generation.

### Python 3!

Frappe Framework and ERPNext are now both compliant with Python 3, the latest and greatest from the Python community. As of Version 11, both Python 2 and 3 are supported and we recommend all users to gradually move to Python 3 as we might drop support for Python 2 in the upcoming versions.

### User Permissions

User Permissions has been redesigned for simplicty and control. In Version 10, setting user permissions depended on 3 settings: User Permissions, Role Permissions, Document Type. This was extremely hard to configure and understand and based on user feedback, we have unlinked Role Permissions from this.

This is the design that actually kicked off a breaking change, and hence Version 11!

[Follow the discussion that led to change in User Permissions](https://discuss.erpnext.com/t/proposal-user-permissions-simplifcation/25641)

<div class="embed-responsive embed-responsive-16by9">
  <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/q37__ttrumA" allowfullscreen></iframe>
</div>

### Auto Repeat

Automatically schedule creation of duplicates of certain documents at fixed intervals. This feature which was restricted to a few document types has now been made generic.

### Workflows

Workflows have been so far a much used but under developed features of Frappe/ERPNext. In Version 11, Workflows are given a much required upgrade. You can now set rules on workflow and track Pending Workflow Action for all users. Users will also get an email notification for their workflow events and they can approve or reject directly via Email!

[Learn More about Workflows](https://erpnext.org/docs/user/manual/en/setting-up/workflows)

### Bulk Actions and Edit

A small tweak that will greatly improve your productivity is Bulk Actions. You can now select and edit a bunch documents from the List View and also Submit and Cancel them. Once you use this feature, you will wonder how did you ever live without it.

<img class="screenshot" alt="Bulk Actions" src="/assets/foundation/img/version-11/bulk-action.gif">

### Dynamic Charts

You can now configure charts on the fly by selecting your axes, powered by the beautiful Frappe Charts library.

### Chat

The in-app chat has been completely revamped and now works real time in an overlay widget. Now start communicating in-app with your colleagues via Frappe Chat

<img class="screenshot" alt="New Chat" src="/assets/foundation/img/version-11/chat.gif">
