import java.util.*;

class login{
    Scanner sc = new Scanner(System.in);

    private String customer_id;
    private String customer_password;
    
    private String customer_id_input;
    private String customer_password_input;

    void info(String customer_id, String customer_password){
        this.customer_id = customer_id;
        this.customer_password = customer_password;
    }

    boolean validate(){
        System.out.println(" --- Welcome to XYZ bank --- ");
        System.out.println("enter customer id : ");
        customer_id_input = sc.next();
        System.out.println("enter password : ");
        customer_password_input = sc.next();

        if(customer_id_input.equals(customer_id) && customer_password_input.equals(customer_password)){
            System.out.println("valid credentials");
            return true;
        }else{
            return false;
        }

    }

}

class open_account{
    Scanner sc = new Scanner(System.in);
    protected static String user_name;
    protected static String user_email;
    
    protected static int user_account_number;;
    protected static int user_PIN;

    void user_info(){
        System.out.println("enter your name : ");
        user_name = sc.nextLine();
        System.out.println("enter your email-id");
        user_email = sc.nextLine();

        char ch1 = '@';
        char ch2 = '.';
        if(user_email.contains(Character.toString(ch1)) && user_email.contains(Character.toString(ch2))){
            System.out.println("valid email-id");
            System.out.println();
            
            user_account_number = (int)(100000*Math.random());
            System.out.println("your generated account number is : "+user_account_number);
           
            user_PIN = (int)(10000*Math.random());
            System.out.println("your generated PIN is : "+user_PIN);

        }else{
            System.out.println("invalid email");
            user_info();
        }

    }

}

class access_account{
    Scanner sc = new Scanner(System.in);
    protected static String user_name;
    protected static int account_no;
    protected static int PIN;

    @SuppressWarnings("static-access")
    
    void login(String user_name,int account_no,int PIN){
        this.user_name = user_name;
        this.account_no = account_no;
        this.PIN = PIN;
    }

    void validate_login_id(){
        int acc_no;
        int Pin;

        System.out.println("enter account number : ");
        acc_no = sc.nextInt();
        if(acc_no == account_no){
            System.out.println("valid account number : ");
        }else{
            System.out.println("invalid account number ");
            validate_login_id();
        }

        System.out.println("enter pin code : ");
        Pin = sc.nextInt();
        if(Pin == PIN){
            System.out.println("valid pin");
        }else{
            System.out.println("invalid Pin code ");
            validate_login_id();
        }
    }

}

class bank_operations1 extends open_account{
    Scanner sc = new Scanner(System.in);
    private double bank_balance;
    private double deposit;
    private int acc_no;
    private int pin;

    void set_balance(){
        System.out.println("deposit atleast 1000 Rs to continue");
        deposit = sc.nextDouble();
        bank_balance+=deposit;
        if(bank_balance<1000){
            double n = 1000-bank_balance;
            System.out.println("not sufficient, please put "+n+" ruppess more ");
        }else{
            System.out.println("please proceed");
        }
    }

    void display_user_information(){
        System.out.println("User Name : "+open_account.user_name);
        System.out.println("Account Number "+open_account.user_account_number);
        System.out.println("Bank balance "+bank_balance);
    }

    void deposit(){
       
        System.out.println("enter account number : ");
        acc_no = sc.nextInt();
        System.out.println("enter PIN : ");
        pin = sc.nextInt();
        if(acc_no == open_account.user_account_number && pin == open_account.user_PIN){
            System.out.println("Please Proceed");
            System.out.println();

            System.out.println("Enter amount to be deposited : ");
            double amount = sc.nextDouble();
                if(amount<100000){
                bank_balance += amount;
                System.out.println("new bank balance "+bank_balance);
            }else{
                System.out.println("you have excedded deposit limit, please try again");
                deposit();
            }
        }else{
            System.out.println("Invalid Credentials");
            deposit();
        }
    }

    void withdraw(){
            System.out.println("enter account number : ");
            acc_no = sc.nextInt();
            System.out.println("enter PIN : ");
            pin = sc.nextInt();

            if(acc_no == open_account.user_account_number && pin == open_account.user_PIN){
            System.out.println("Please Proceed");
            System.out.println();
        
            System.out.println("enter amount to be withdrawn : ");
            double amount = sc.nextDouble();
                if(amount<100000){   
                bank_balance -= amount;
                System.out.println("new bank balance : "+bank_balance);
            }else{
                System.out.println("you have excedded withdraw limit, please try again");
                withdraw();
            }
        }else{
            System.out.println("Invalid Credentials");
            withdraw();
        }
    }
}

class bank_operations2 extends access_account{
    Scanner sc = new Scanner(System.in);
    private double bank_balance;
    private double deposit;
    private int acc_no;
    private int pin;

    void set_balance(double bank_balance){
        this.bank_balance = bank_balance;
    }

    void display_user_information(){
        System.out.println("User Name : "+access_account.user_name);
        System.out.println("Account Number "+access_account.account_no);
        System.out.println("Bank balance "+bank_balance);
    }

    void deposit(){
       
        System.out.println("enter account number : ");
        acc_no = sc.nextInt();
        System.out.println("enter PIN : ");
        pin = sc.nextInt();
        if(acc_no == access_account.account_no && pin == access_account.PIN){
            System.out.println("Please Proceed");
            System.out.println();

            System.out.println("Enter amount to be deposited : ");
            double amount = sc.nextDouble();
                if(amount<100000){
                bank_balance += amount;
                System.out.println("new bank balance "+bank_balance);
            }else{
                System.out.println("you have excedded deposit limit, please try again");
                deposit();
            }
        }else{
            System.out.println("Invalid Credentials");
            deposit();
        }
    }

    void withdraw(){
            System.out.println("enter account number : ");
            acc_no = sc.nextInt();
            System.out.println("enter PIN : ");
            pin = sc.nextInt();

            if(acc_no == access_account.account_no && pin == access_account.PIN){
            System.out.println("Please Proceed");
            System.out.println();
        
            System.out.println("enter amount to be withdrawn : ");
            double amount = sc.nextDouble();
                if(amount<100000){   
                bank_balance -= amount;
                System.out.println("new bank balance : "+bank_balance);
            }else{
                System.out.println("you have excedded withdraw limit, please try again");
                withdraw();

            }
        }else{
            System.out.println("Invalid Credentials");
            withdraw();
        }
    }


}

public class bank{
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        login customer = new login();
        customer.info("2241013165", "Rishi2004");
        if(customer.validate()){
            System.out.println("Create New Account / Log in to Existing Account (Press 1 / Press 2)");
            int n = sc.nextInt();
            if(n==1){
                open_account A = new open_account();
                A.user_info();
                bank_operations1 B = new bank_operations1();
                B.set_balance();
                int choice;

                do {
                    System.out.println("\n --- Banking System Application ---");
                    System.out.println(" 1.Display account details\n 2.Deposit the amount\n 3.Withdraw the amount\n 4.Exit ");
                    choice = sc.nextInt();
            
                        switch (choice){
                            case 1:
                                B.display_user_information();
                                break;
                            case 2:
                                B.deposit();
                                break;
                            case 3:
                                B.withdraw();
                                break;
                            case 4:
                                System.out.println("--- Thanks for visiting --- \n --- Wish you a good day --- ");
                    }
                }while(choice<4 && choice>0);

            }

            if(n==2){
                access_account A = new access_account();
                A.login("Rishivatsal Mishra", 22410, 2004);
                A.validate_login_id();

                bank_operations2 B = new bank_operations2();
                B.set_balance(10000);
                int choice;

                do {
                    System.out.println("\n --- Banking System Application ---");
                    System.out.println(" 1.Display account details\n 2.Deposit the amount\n 3.Withdraw the amount\n 4.Exit ");
                    choice = sc.nextInt();
            
                        switch (choice){
                            case 1:
                                B.display_user_information();
                                break;
                            case 2:
                                B.deposit();
                                break;
                            case 3:
                                B.withdraw();
                                break;
                            case 4:
                                System.out.println("--- Thanks for visiting --- \n --- Wish you a good day --- ");
                    }
                }while(choice<4 && choice>0);

            }
        }else{
            System.out.println("invalid choice, please try again");
        }
       sc.close();
    }
}
