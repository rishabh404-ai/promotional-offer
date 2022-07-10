# promotional-offer

# tortoise-assignment

> **Task**:

    Functionality on the brand partner side
          1. Brand partner creates a plan
                a. Creates a plan in the database with planID, planName, amountOptions and
                tenureOptions, benefitPercentage (for example: 10), benefitType
                (cashback/extraVoucher) and any other attributes needed. 
          2. Brand partner creates promotion for an existing plan
                a. Promotion can be limited in two ways
                      i. By the number of users to get the promotion (for example: 500 users)
                      ii. By a time period (for example: 22th May 2022 to 24th May 2022)
          b. Assume that promotion can only affect benefitPercentage for a given plan
          
    Functionality on the end-user side
          1. List the available plans on the platform or the brand
          2. Enroll in any of the plans
                  a. Create an entry in the CustomerGoals table with the planID, userID, selectedAmount, selectedTenure, startedDate, depositedAmount, benefitPercentage, benefitType and any other attributes needed.
    Design the system to create promotions on plans and show updated information to users based on the respective promotion type. 
    CustomerGoals table should capture the right information on the benefitPercentage based on the promotions.
    
> **How to get the project running ?**

     1. Create an virutal env & activate it.
        Run > virtualenv <env-name>
            > source <env-name>/bin/activate

     2. RUN the following commands:
                 > pip3 install -r requirements.txt 
                 > python3 manage.py runserver

> **IMPORTANT POINTS TO REMEMBER**:

      1. No customer login is created for this task. Customer-goals API will require authentication. 
         Try login via superuser through admin panel for this task.
         cred for superuser > user : admin, pass : admin
         admin url can be accessed through > localhost/admin
         If you wanna create your own: 
                  RUN > python manage.py createsuperuser
      
      2. I have added a feature of cashback_amount. This field will grab the total cashback amount that the user will recieve depending
         on the plan he enrolled and the benefit percentage related to that specific plan. 
         
         If the payment is not recieved from the user, then the customer_active_plan will be set to False and also the payment field will be False.
         Hence, the cashback amount will further be auto-set to Null
         
         Cashback will only be calculated if the user's payment is recieved during plan enrollment.

      3. I've tried capturing all the transactions or plan enrollements that the user has tried to enroll in. Even if the user fails to purchase
         a plan due to payment issue or failure, the API captures that also so that we can have a record of everything (even failures).
         
         But for viewing the active/purchased/enrolled plan of a user, we can refer **localhost/customer-goals/customer_active_plans/**
         
         Again there is an API of seeing failed transaction also which you will find the listing as you read below :)
       
      4. I haven't added functionality to the user to manually add fields such as selectedAmount, selectedTenure, depositedAmount,
         benefitPercentage, benefitType. Instead these all will be dynamically set by the API. User only need to select the promotional plan
         he viewed and just enroll in it. All the payment amount and other data will be fetched by the API and stored in db and so there will be no manual
         process just to be on safer side. The data will be fetched from the plan details to which the user is enrolling and so the payment amount will be
         restricted and will be unchangable for security reasons. This will ensure that all the data is correct.
       
       5. In customer-goals, As we don't have a payment system for this task, so i have added a check during posting data for this API. 
          If check is true, meaning the payment has been recieved from the user.


> **Endpoints**

     **FOR BRAND**

     1. API Endpoint to create a plan

        localhost/plans/

     2. API Endpoint to create a promotion for an existing plan

        localhost/promotions/
        
     **FOR END USERS**   
      
     3. API Endpoint to enroll in a plan by end-user
        localhost/customer-goals/
        
     4. API Endpoint to filter all the enrolled plans of users which 
        got success with their payments and hence are active.
        
        localhost/customer-goals/customer_active_plans/
        
     5. API Endpoint to filter all the transactions of users which 
        got failed due to payment failure and hence failing to active their plans.
        
        localhost/customer-goals/customer_failed_transactions/
        
     6. API Endpoint to display list of all available plans to end-user
     
        localhost/available-plans/
        
     7. API Endpoint to display list of all active promotions to end-user
        Users can also filter the promotions based on parameters promo_name and/or promo_type
        
        localhost/active-promotions/
        
        localhost/active-promotions/?promo_name={promo_name}&promo_type={promo_type}
        
        OR
        
        localhost/active-promotions/?promo_name={promo_name}
        localhost/active-promotions/?promo_type={promo_type}
        
        IT ALL DEPENDS ON WHAT YOU WANNA FILTER !!
        
        


       
Please let me know if you have any queries

Rishabh Mishra

mishrarishabh404it@gmail.com
