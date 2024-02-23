import java.util.Scanner;

class bank_users {
    Scanner sc = new Scanner(System.in);
    public String account_no;
    public String user_name;
    public String account_type;
    public double bank_balance;

    //Opening new Account -:

    public void open_account() {

        System.out.println("enter Name : ");
        user_name = sc.nextLine();

        System.out.println("enter account number : ");
        account_no = sc.next();

        System.out.println("enter account type (saving/salary/FD) : ");
        account_type = sc.next();

        System.out.println("enter account's bank balance : ");
        bank_balance = sc.nextLong();
    }
    //Displaying Bank Information -:

    public void account_info(){
        System.out.println("Name of user : "+user_name+"\n"+"Account number :"+account_no +"\n"+"Type of Account : "+account_type +"\n"+"Account Balance : "+bank_balance+"\n");
    }

    //Method to Deposit Money -:

    public void deposit_money(){

        System.out.println("Enter amount to be deposited : ");
        double amount = sc.nextDouble();
        bank_balance += amount;
        System.out.println("new balance : "+bank_balance);
    }


    //Method to Withdraw Money -:
    public void withdraw_money() {
        System.out.println("enter amount to be withdrawn : ");
        double amount = sc.nextDouble();
        bank_balance -= amount;

        if (bank_balance < amount) {
            System.out.println("withdrawal not possible");
        } else {
            System.out.println("new balance : " + bank_balance);
        }

    }
    //Searching user -:
    public boolean search_user(String input_account_no){
        if(input_account_no.equals(account_no)){
            account_info();
            return true;
        }
        return false;
    }

}

public class multi_bank {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter number of users (1 to 4) : ");
        int n = sc.nextInt();
        bank_users[] users = new bank_users[n];

        for(int i = 0;i< users.length;i++){
            users[i] = new bank_users();
            users[i].open_account();
        }

        int choice;
        do{
            System.out.println("--- Banking System Application --- \n");
            System.out.println(" 1. Display all account details \n 2. Search by Account number\n 3. Deposit the amount \n 4. Withdraw the amount \n 5.Exit ");
            System.out.println("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice){
                case 1:
                    for(int i =0;i<users.length;i++){
                        users[i].account_info();
                    }
                    break;
                case 2:
                    System.out.println("enter account to be searched : ");
                    String input_account_no = sc.next();
                    boolean result = false;
                    for(int i = 0;i<users.length;i++){
                        result = users[i].search_user(input_account_no);
                        if(result){
                            break;
                        }
                    }
                    if(!result){
                        System.out.println("account dosen't exist");
                    }
                    break;
                case 3:
                    System.out.print("Enter Account no. : ");
                    input_account_no = sc.next();
                    result = false;
                    for (int i = 0; i < users.length; i++) {
                        result = users[i].search_user(input_account_no);
                        if (result) {
                            users[i].deposit_money();
                            break;
                        }
                    }
                    if (!result) {
                        System.out.println("Search failed! Account doesn't exist..!!");
                    }
                    break;
                case 4:
                    System.out.print("Enter Account No : ");
                    input_account_no = sc.next();
                    result = false;
                    for (int i = 0; i < users.length; i++) {
                        result = users[i].search_user(input_account_no);
                        if (result) {
                            users[i].withdraw_money();
                            break;
                        }
                    }
                    if (!result) {
                        System.out.println("Search failed! Account doesn't exist..!!");
                    }
                    break;
                case 5:
                    System.out.println("See you soon...");
            }
        }while (choice>0 && choice<5);

    }
}
