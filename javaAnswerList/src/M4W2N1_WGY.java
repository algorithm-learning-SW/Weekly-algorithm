public class M4W2N1_WGY {
    public static void main(String[] args){
        System.out.println(finalDaejin(16,1,7));
    }

    public static int  finalDaejin(int n, int a, int b){
        // 2로 나누고 > 뭘 더해야하는 것 같은데
        int answer = 0;

        // 계속해서 채번을 해주고 서로 겨루는 경우마다 answer+1을 해주고 대진표가 1 2 3 4 > 1 2 > 1(최종)이니까 같아 지는 순간에 answer를 return하면 될것같음
        // for문은 내가 끝나는 횟수를 알아야하는데 그거구하느니.. while문으로 계속 겨룸 > 가지고 있는 숫자가 같아지면 break
        // (현재 자신의 번호+1) / 2 = 다음 라운드에서의 번호니까.. 12 > 1 , 34 > 2

        while(true){
            a = (a+1)/2;
            b = (b+1)/2;
            answer++;
            if(a==b){
                break;
            }
        }
        // 오케이 통과 ㅋㅋ
        // 풀고나서 보니까 b/2 + b%2;라고 산정한사람들이 있는데 이건 뭐임?? 오ㅑ 나머지를 더하지??
        // 아 위에거 풀어쓴건가보다 위에는 몫을 무조건 나오도록하는거면 다른식은 홀수의 나머지를 더하는느낌

        return answer;
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
