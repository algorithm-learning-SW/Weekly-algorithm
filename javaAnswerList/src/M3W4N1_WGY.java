import java.util.Arrays;

public class M3W4N1_WGY {
    public static void main(String[] args){
        int Qnum = 4;
        // 4 > [1,2,9,3,10,8,4,5,6,7]
        // 5 > [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
        System.out.println(Arrays.toString(solution(Qnum)));
    }

    public static int[] solution(int n) {

        // 1. array가 총 몇개가 될건지 예측 > 등차수열
        int[] answer = new int[(n*(n+1))/2];


        // 2. for문의 구도 파악 삼각형의 층과 밑변을 훑어야하니, 층 n번 밑변 n변을 훑는다 생각해 > 2중 for문
        // answer 인덱싱을 위한 count 변수, for문을 도는동안 array에 값이 추가될때마다 count++;
        // 3. for문에서 삼각형을 지그재그로 돌지, 달팽이 모양으로 돌지 생각해야함. 지그재그로 돌면 구현이 안됨
        // 그래서 달팽이 모양으로 돌려면 ↙ → ↖.. 무조건 2차원 배열로 생각해서 풀어야하나봄
        // 2차원배열 > 1차원으로 풀어주기

        // 2차원 배열을 만들어내는 for문
        int[][] matrix = new int[n][n];

        // x,y 좌표 & array에 담길 숫자
        int x = -1, y = 0;
        int num = 1;

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                // 삼각형의 대각선을 타고 array를 순회하는 식
                // n*n 사각형
                // 1 0 0 0
                // 2 9 0 0
                // 3 10 8 0
                // 4 5 6 7

                if (i % 3 == 0) {
                    x++;
                } else if (i % 3 == 1) {
                    y++;
                } else if (i % 3 == 2) {
                    x--;
                    y--;
                }
                matrix[x][y] = num++;
            }
        }

        System.out.println(Arrays.deepToString(matrix));

        // 그걸 1차원으로 변경
        int k = 0;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(matrix[i][j] == 0)
                    break;
                answer[k++] = matrix[i][j];
            }
        }

        // 아쉬운점.. 무조건 2차원을 거쳐서 사고해야하는가
        return answer;
    }
}
