public class Main {

    public static void main(String[] args) {
        Book java_book = new Book("JAVA", "OSAMA", 2022, 890);

        java_book.OpenBook();
//        boolean result = java_book.MoveToPage(200);
//        System.out.print(result);
        java_book.PrintBookInfo();
        java_book.CloseBook();
    }
}