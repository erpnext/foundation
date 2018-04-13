// Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ready(function(){

    var searchButton = document.querySelector(".js-search-icon");
    var searchForm = document.querySelector(".js-search-form");
    var searchInput = document.querySelector(".js-search-input");
    var searchInputButton = document.querySelector(".js-search-input-icon");

    searchButton.addEventListener("click", function(){
        searchForm.classList.remove("display-none");
    });

    searchInput.addEventListener("blur", function(){
        // this is not working... todo_fn
        searchForm.classList.add("display-none");
    }, false)

    searchInputButton.addEventListener("click", function(){
        searchForm.classList.add("display-none");
    })
})