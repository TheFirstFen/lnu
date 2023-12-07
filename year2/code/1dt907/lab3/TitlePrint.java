public class TitlePrint {
    public static void printTask(String problemTitle) {
        int width = 40;
        int height = 10;
        String text = problemTitle;

        System.out.print("╔");
        for (int i = 0; i < width - 2; i++) {
            System.out.print("═");
        }
        System.out.println("╗");

        int remainingVerticalSpace = height - 2;
        int topSpace = remainingVerticalSpace / 2;
        int bottomSpace = remainingVerticalSpace - topSpace;

        for (int i = 0; i < topSpace; i++) {
            System.out.print("║");
            for (int j = 0; j < width - 2; j++) {
                System.out.print(" ");
            }
            System.out.println("║");
        }

        int remainingSpace = width - 2 - text.length();
        int leftSpace = remainingSpace / 2;
        int rightSpace = remainingSpace - leftSpace;
        System.out.print("║");

        for (int j = 0; j < leftSpace; j++) {
            System.out.print(" ");
        }

        System.out.print(text);

        for (int j = 0; j < rightSpace; j++) {
            System.out.print(" ");
        }
        System.out.println("║");

        for (int i = 0; i < bottomSpace; i++) {
            System.out.print("║");
            for (int j = 0; j < width - 2; j++) {
                System.out.print(" ");
            }
            System.out.println("║");
        }

        System.out.print("╚");
        for (int i = 0; i < width - 2; i++) {
            System.out.print("═");
        }
        System.out.println("╝");
    }
}
