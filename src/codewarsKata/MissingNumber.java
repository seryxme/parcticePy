package codewarsKata;

public class MissingNumber {
    public static void main(String[] args) {
        int[] numbers = {4, 2, 1};

        System.out.println(findMissing(numbers));

    }

    public static int findMissing(int[] numbers) {
        int[] differences = new int[numbers.length - 1];

        for (int i = 0; i < numbers.length - 1; i++) {
            differences[i] = numbers[i + 1] - numbers[i];
        }

        int missingNum = numbers[numbers.length - 1] + differences[differences.length - 1];

        for (int i = 0; i < differences.length - 1; i++) {
            if (differences[i + 1] - differences[i] != 0) {
                if (differences[i] > differences[i + 1]) missingNum = numbers[i] + differences[i + 1];
                else missingNum = numbers[i + 1] + differences[i];
                break;
            }
        }
        return missingNum;
    }
}
