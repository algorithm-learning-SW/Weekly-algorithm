import java.util.*;
import java.util.stream.Stream;

public class M4W3N1_WGY {

    public static void main(String[] args){
        // 이건 main함수라 그냥 건들지 ㅏㅇㄶ겠음..
        solution1(5);
    }

    public static int solution1(int n) {
        // 7 -> 3
        int two_cases = n/2;

        System.out.println(two_cases);

        ArrayList<Integer>[] two_array = new ArrayList[two_cases];

        for (int i = 0; i <= two_cases; i++){

            System.out.println(i);
//            two_array[i] = new ArrayList<Integer>();
//            for(int j = 0; j <= i; j++){
//                // 0인 경우가 패스가 되나?
//                two_array[i].add(2);
//            }
        }

//        System.out.println(Arrays.deepToString(two_array));

        int result= 0;
        return result;
    }



    public int solution2(int n) {
        int answer = 0;

        int[] arr = new int[n];
        arr[0] = 1;
        arr[1] = 2;

        for (int i = 2; i < n; i++) {
            int num = arr[i - 1] + arr[i - 2];
            arr[i] = num % 1000000007;
        }

        return arr[n-1];
    }

}
