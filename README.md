<!-- Output copied to clipboard! -->

<!-----

You have some errors, warnings, or alerts. If you are using reckless mode, turn it off to see inline alerts.
* ERRORs: 0
* WARNINGs: 0
* ALERTS: 1

Conversion time: 0.708 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β34
* Tue May 23 2023 06:54:10 GMT-0700 (PDT)
* Source doc: Proof Of Concept Dynamic Roles and Permissions Database Less
* This document has images: check for >>>>>  gd2md-html alert:  inline image link in generated source and store images to your server. NOTE: Images in exported zip file from Google Docs may not appear in  the same order as they do in your doc. Please check the images!

----->

<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 0; ALERTS: 1.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>

# Proof Of Concept Dynamic Roles and Permissions Database Less

## Introduction

Database query time can be a bottleneck in application performance. Static roles and permissions can lead to users being granted permissions they don't need, which can increase the number of database queries.

This proof of concept will demonstrate how dynamic roles and permissions can be used to reduce database query time and significantly simplify the control actions buttons in the front-end.

## Key Concept

I suppose using the addition of 2^n sequence to provide the permissions which users have. This means we are able to get a list of permissions from a single line of numbers.

Assume that we have list persmins as I showing below:

<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image1.png "image_tooltip")

**In the traditional way** we have to bind a relationship role with any of the permissions above and query every request time and UI displaying.

If we have a role named general_user which can only view what we have to store, general_user has permission id 1 and general_user has permission id 2 in the database, and we have to query this and verify every time.

**For the new approach** we store only the sum of permission id 1 and permission id 2 (it must be 3) which belong to the general_user role in db. In the verify stage we only use the verify function which reverses the process of sum in order to define permission id 1 and 2.

Example:

Role A have permission [1,4,16,64] => sum of role A = 85

From 85 we are able to get [1,4,16,64] based on an algorithm in github.

The key is we are able to get specific numbers (2^?) from the sum of 2^x. We are able to verify permission without a database with a sample of function if we map our permission id to our route and ui hide/how.

## Logical proof using mathematical reasoning

To prove that the sum of any numbers in the sequence 2^n, where x is a whole number, is not equal to any number in the sequence that has not yet been included in the sum, we can use a proof by contradiction.

Assume that there exists a sum of numbers in the sequence that is equal to a number in the sequence that has not been included in the sum. Let's represent the numbers in the sequence as a1, a2, a3, ..., an, where n is the total number of numbers in the sequence.

According to our assumption, there exists a sum of numbers, let's say ai1 + ai2 + ai3 + ... + aim, that is equal to a number in the sequence, aj, where j > m and j ≤ n.

Now, let's consider the sum of all the numbers in the sequence, which can be represented as:

a1 + a2 + a3 + ... + an

Since the sequence is in ascending order, each subsequent number is greater than the sum of all the previous numbers. Therefore, we have:

a1 &lt; a1 + a2

a1 + a2 &lt; a1 + a2 + a3

a1 + a2 + a3 &lt; a1 + a2 + a3 + a4

...

a1 + a2 + a3 + ... + an-1 &lt; a1 + a2 + a3 + ... + an

Thus, we can conclude that the sum of any subset of numbers from the sequence is strictly less than the sum of all the numbers in the sequence.

However, in our assumption, we stated that there exists a subset sum equal to a number in the sequence that has not been included in the sum. This contradicts the fact that the subset sum is always strictly less than the sum of all the numbers in the sequence.

Therefore, we have proven that the sum of any numbers in the sequence 2^n, where x is a whole number, is not equal to any number in the sequence that has not yet been included in the sum.
