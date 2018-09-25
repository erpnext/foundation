<!-- add-breadcrumbs -->
# Global Search

Global-search.md


Global search is a word-processing operation in which a complete computer file or set of files is searched for every occurrence of a particular word or other sequence of characters.

We have made the Awesome Bar of ERPNext lot more powerful by adding Global Search feature. 
Global Search helps users find information quickly. It’s located in the upper right-hand corner in ERPNext.  Simply entering a few characters in the Search will show results from several different record types (Contact, Customer, Issues etc.) related to that keyword. You can also customise the fields based on which search will be shown.

From v11, multi search term/keywords separated by & operator is supported, refer to the following use cases
. input "apple & ipod" can return docs with one field contain Apple and the other contains Ipod( PO's vendor and item?)
. input "iphone & ipod" can return target docs which contain both item iphone and Ipod (child table items)
. input "iphone & black" can return item with description contains both iphone and black(long text field)
. input 'foo & bar" can return any docs with both tags foo and bar assigned.(special long text field _usertags)

### Using Awesome bar for Global Search.

<img alt="Global Search" class="screenshot" src="{{docs_base_url}}/assets/img/articles/Global Search .gif">

### Enable Global Search for fields in a Doctype.

<img alt="Global Search" class="screenshot" src="{{docs_base_url}}/assets/img/articles/Enable Global Search .gif">

