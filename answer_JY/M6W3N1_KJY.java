import java.util.*;

public class M6W3N1_KJY {
    public static ArrayList<int[]> permu=new ArrayList<int[]>();
    
    public static void permute(int[] arr){
        permuteHelper(arr, 0);
    }

    private static int[] permuteHelper(int[] arr, int index){
        if(index >= arr.length - 1){ //If we are at the last element - nothing left to permute
        return arr;
    }

    for(int i = index; i < arr.length; i++){ //For each index in the sub array arr[index...end]

        //Swap the elements at indices index and i
        int t = arr[index];
        arr[index] = arr[i];
        arr[i] = t;

        //Recurse on the sub array arr[index+1...end]
        int[] subpermu=permuteHelper(arr, index+1);
        permu.add(subpermu);
        //Swap the elements back
        t = arr[index];
        arr[index] = arr[i];
        arr[i] = t;
    }
    return arr;
}
    /*
    private void swap(int[] input, int a, int b) 
    {
        int tmp = input[a];
        input[a] = input[b];
        input[b] = tmp;
    }
    
    public void permutation(int n, ArrayList<int[]> elements)
    {
        int[] indexes = new int[n];
        for (int i = 0; i < n; i++) {
            indexes[i] = 0;
        }

        int i = 0;
        while (i < n) {
            if (indexes[i] < i) {
                swap(elements, i % 2 == 0 ?  0: indexes[i], i);
                indexes[i]++;
                i = 0;
            }
            else {
                indexes[i] = 0;
                i++;
            }
        }
    }
    */
    public int solution(int n, String[] data) {
        permute(new int[]{1,2,3,4,5,6,7,8});
        
        Map<String, Integer> hash=new HashMap<String, Integer>();
        hash.put("A", 1);
        hash.put("C", 2);
        hash.put("F", 3);
        hash.put("J", 4);
        hash.put("M", 5);
        hash.put("N", 6);
        hash.put("R", 7);
        hash.put("T", 8);
        
        ArrayList<int[]> cond=new ArrayList<int[]>();
        
        int i=0;
        for(i=0;i<n;i++)
        {
            String input=data[i];
            int axis1=hash.get(input.charAt(0));
            int axis2=hash.get(input.charAt(2));
            int distance=Integer.parseInt(String.valueOf(input.charAt(4)));
            int conditional=0;
            if(input.charAt(3)=='=')
                conditional=0;
            if(input.charAt(3)=='>')
                conditional=-1;
            if(input.charAt(3)=='<')
                conditional=1;
            int[] encode={axis1, axis2, conditional, distance};
            cond.add(encode);
        }
        
        System.out.println("Permutation : "+permu);
        /*
        int j=0;
        for(j=0;j<n;j++)
        {
            int[] code=cond[j];
               
                
        }
        */
        return 0;


    }

    public static void main(String[] args)
    {
        int a=solution(2, ["N~F=0", "R~T>2"]);
        System.out.println(a);
        return;
    }
}