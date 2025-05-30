import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int r = scan.nextInt();
        int c = scan.nextInt();
        int confetti = scan.nextInt();
        int k = scan.nextInt();

        ArrayList<Node> list = new ArrayList<>();
        for(int i = 0; i < k; i++) {
            list.add(new Node(scan.nextInt(),scan.nextInt()));
        }
        Collections.sort(list);

        int left = 1;
        int right = Math.min(r, c);
        while(left <= right) {
            int mid = (left + right) / 2;

            if(can_blind(mid, confetti, list)) {
                right = mid - 1;
            } else left = mid + 1;
        }
        System.out.println(left);
    }

    public static boolean can_blind(int m, int confetti, ArrayList<Node> list) {
        int count = 0;
        int pre = 0;
        for(int i = 0; i < list.size(); i++) {
            Node current = list.get(i);
            if(current.x > m) return false;
            if(pre == 0 || pre + m <= current.y) {
                pre = current.y;
                count++;
                if(count > confetti) return false;
            }
        }
        return true;
    }

    public static class Node implements Comparable<Node> {
        int x;
        int y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(Node n) {
            return this.y - n.y;
        }
    }
}
