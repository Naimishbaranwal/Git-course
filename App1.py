import os



# os.getcwd()

class Bill_payable:
    """Bill paid by tenant for particular month with particular amount """
    def __init__(self,month,amount):
        self.month=month
        self.amount=amount
        
class Tenants:
    """Tenant names and number of days tenant spend in house and total amount pays by tenant with respect to number of days spend in house."""
    def __init__(self,name,number_days):
        self.name=name
        self.number_days=number_days

    def payment_tenant(self,bill,other_tenant_days):
        return (self.number_days/(self.number_days+other_tenant_days))*bill.amount


if __name__ == "__main__":

    month=input("Enter the month name: ")
    amount=float(input("Enter the total amount: "))
    name1=input("Enter the tenant1 name: ")
    day1=int(input("Enter the tenant1 days: "))
    name2=input("Enter the tenant2 name: ")
    day2=int(input("Enter the tenant2 days: "))


    bill_t=Bill_payable(month,amount)
    tenant1=Tenants(name1,day1)
    tenant2=Tenants(name2,day2)
    pay1=tenant1.payment_tenant(bill_t,tenant2.number_days)
    print(f'total rent for the month {bill_t.month} is {bill_t.amount}')
    print(f"For {name1} the total rent for the {bill_t.month} month is: {round(pay1,2)}")
    pay2=tenant2.payment_tenant(bill_t,tenant1.number_days)
    print(f"For {name2} the total rent for the {bill_t.month} month is: {round(pay2,2)}")
