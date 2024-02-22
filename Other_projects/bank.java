import java.util.*;
class bank_user{
    Scanner sc = new Scanner(System.in);
    private String account_no;
    private String user_name;
    private String account_type;
    private double bank_balance;

    //Opening new Account -:

    public void open_account() {

        System.out.println("enter Name : ");
        user_name = sc.nextLine();

        System.out.println("enter account number : ");
        account_no = sc.next();

        if (account_no.length() != 10) {
            System.out.println("length of account number");
        }

        System.out.println("enter account type : ");
        account_type = sc.next();

        System.out.println("enter account's bank balance : ");
        bank_balance = sc.nextLong();
    }
    //Displaying Bank Information -:

    public void account_info(){
        System.out.println("Name of user : "+user_name);
        System.out.println("Account number : "+account_no);
        System.out.println("Type of Account : "+account_type);
        System.out.println(" Account Balance : "+bank_balance);
    }

    //Method to Deposit Money -:

    public void deposit_money(){

        System.out.println("Enter amount to be deposited : ");
        double amount = sc.nextDouble();
        bank_balance += amount;
        System.out.println("new balance : "+bank_balance);
    }

    //Method to Withdraw Money -:
    public void withdraw_money(){
        System.out.println("enter amount to be withdrawn : ");
        double amount = sc.nextDouble();
        bank_balance -= amount;

        if(bank_balance<amount){
            System.out.println("withdrawal not possible");
        }else{
            System.out.println("new balance : "+bank_balance);
        }
    }

}



class bank{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        bank_user user = new bank_user();
        user.open_account();

        System.out.println("\n --- Banking System Application ---");
        System.out.println("1. Display account details \n 2. Deposit the amount \n 3. Withdraw the amount \n 4.Exit ");
        int choice = sc.nextInt();

        switch (choice){
            case 1:
                user.account_info();
            case 2:
                user.deposit_money();
            case 3:
                user.withdraw_money();
            case 4:
                System.out.println("--- Thanks for visiting --- \n --Wish you a good day-- ");
        }

    }
}