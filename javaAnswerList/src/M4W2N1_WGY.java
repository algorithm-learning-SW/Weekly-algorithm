public class M4W2N1_WGY {
    public static void main(String[] args){
        System.out.println("s");
    }

    public static int Daejin(int n, int a, int b){

        // 12 34 56 78
        // 1   2  3  4 니까.. 뭔가 4-2+1 해주면 되는거 아냐? 라고 생각해서 나온 로직
        // 가 틀려서 몫을 따주고 해당값이 홀수면 +1 해주면 되겠군 한거

        int s1 = oddT((a)/2);
        System.out.println(s1);
        int s2 = oddT((b)/2);
        System.out.println(s2);

        int answer = s2-s1+1;

        // 인데 틀렸고.. ㅏ 뭔가 여기서... 조금만 더하면 풀릴거같은데 근데 n의 존재가 왜있는겨?싶엇음

        return answer;

    }

    // 홀수이면 추가해주는 함수
    public static int oddT(int w){
        if(w%2 == 1){
            w = w+1;
        }
        return w;
    }

    public static int ex_Daejin(int n, int a, int b){

        // 12 34 56 78
        // 1   2  3  4 니까.. 뭔가 4-2+1 해주면 되는거 아냐? 라고 생각해서 나온 로직

        int s1 = (a+1)/2;
        System.out.println(s1);
        int s2 = (b+1)/2;
        System.out.println(s2);


        int answer = s2-s1+1;

        // System.out.println("Hello Java");

        return answer;

    }

}
