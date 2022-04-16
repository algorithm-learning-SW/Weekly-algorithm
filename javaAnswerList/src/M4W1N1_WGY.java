import java.util.Arrays;
import java.util.stream.Stream;

public class M4W1N1_WGY {
    
    public static void main(String[] args){
        // 이건 main함수라 그냥 건들지 ㅏㅇㄶ겠음..
    }

    
    // 1트 > 장렬히 실패
    public String solution1(String s) {
        // 1. Str을 array에 집어넣어줌
        String[] strData = s.split(" ");
        
        // 2. 집어넣은 strData갯수만큼의 숫자 array 생성
        int[] intData = new int[strData.length];
        
        // 3. stream으로 for문없이 하나하나 strData intData로 변경(아 이렇게 안되나?)
        //for(int=0;)
            // 아.. 보니까 for문으로만 가능한거같음 stream을 쓰려면 아예 integer이라는 형식이어야함
        
        
        String answer = "";
        return answer;
    }

    public String solution2(String s) {
        // 1. Str을 array에 집어넣어줌
        String[] strData = s.split(" ");
        
        // 2. integer array로 stream시도
        // stream은 자바8에서 새로 나온 병렬처리 api임
        Integer[] intData = Stream.of(strData).mapToInt(Integer::parseInt).boxed().toArray(Integer[]::new);
        
        // 3. int arr에서 최소최대 찾기, 정렬 > 인덱싱 > int To str
        Arrays.sort(intData);
        
        // 4. answer같은 경우엔 최소 + "공백" + 최대 이렇게해서 한번에 출력
        String answer = Integer.toString(intData[0]) + " " + Integer.toString(intData[intData.length - 1]);
        return answer;
        
    }

}