#include<bits/stdc++.h>
using namespace std;
struct Node
{
    int data;
    struct Node *left;
    struct Node *right;
    int height;
};
int heigh(struct Node* Node)
{
    /* base case tree is empty */
    if(Node == NULL)
        return 0;

    /* If tree is not empty then height = 1 + max of left
       height and right heights */
    return 1 + max(heigh(Node->left), heigh(Node->right));
}
bool isBalanced(struct Node *root)
{
    int lh; /* for height of left subtree */
    int rh; /* for height of right subtree */

    /* If tree is empty then return true */
    if(root == NULL)
        return 1;

    /* Get the height of left and right sub trees */
    lh = heigh(root->left);
    rh = heigh(root->right);

    if( abs(lh-rh) <= 1 &&
        isBalanced(root->left) &&
        isBalanced(root->right))
        return 1;

    /* If we reach here then tree is not height-balanced */
    return 0;
}

/* UTILITY FUNCTIONS TO TEST isBalanced() FUNCTION */

/* returns maximum of two integers */


/*  The function Compute the "height" of a tree. Height is the
    number of Nodes along the longest path from the root Node
    down to the farthest leaf Node.*/
int _B_(Node *root)
{
    if(root==NULL)
        return 0;
    int lH = _B_(root->left);
    if(lH==-1)return -1;
    int rH = _B_(root->right);
    if(rH==-1)
        return -1;
    if(abs(lH-rH)>1)
        return -1;
    return max(lH,rH)+1;
}
bool _B(Node *root)
{
    if(_B_(root)==-1)
        return false;
    else
        return true;
}
bool I_(Node* root)
{
    static struct Node *prev = NULL;

    if (root)
    {
        if (!I_(root->left))
            return false;

        if (prev != NULL && root->data <= prev->data)
            return false;

        prev = root;

        return I_(root->right);
    }

    return true;
}
Node* insertToAVL(Node* Node, int data);
vector<int> z;
void inorder(Node *root)
{
//	z.clear();
    if(root==NULL)
        return;
    {
        inorder(root->left);
        z.push_back(root->data);
        inorder(root->right);
    }
}
/* Drier program to test above function*/
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int q;
        cin>>q;
        Node *root = NULL;
        bool f= true;
        vector<int> a;
        while(q--)
        {
            int k;
            cin>>k;
            a.push_back(k);
            root = insertToAVL(root,k);
            if(!isBalanced(root)){
                f=false;
                break;
            }
        }

        z.clear();

        inorder(root);

        set<int> s(a.begin(),a.end());
        vector<int>zz(s.begin(),s.end());
        if(z.size()!=zz.size())
            f=false;
        else{
            for(int i=0;i<z.size();i++)
            {
                if(z[i]!=zz[i])
                    f=false;
            }
        }
        if(f)
            cout<<1<<endl;
        else
            cout<<0<<endl;
    }
    return 0;
}

/*Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above.*/

/* The structure of the Node is
struct Node
{
    int data;
    Node *left;
    Node *right;
    int height;
};
 

*/


/* ************************** */

Node* rotateNode(Node* z, const string& mode) {
    Node* y;
    if (mode == "r") {
        y = z->left;
        Node* t3 = y->right;
        y->right = z;
        z->left = t3;
    } else {  // mode == "l"
        y = z->right;
        Node* t2 = y->left;
        y->left = z;
        z->right = t2;
    }
    // update height
    y->height = heigh(y);
    z->height = heigh(z);
    return y;
}

Node* balanceNode(Node* z, const string& mode) {
    if (mode == "ll") {
        z = rotateNode(z, "r");
    } else if (mode == "lr") {
        Node* y = z->left;
        z->left = rotateNode(y, "l");
        z = rotateNode(z, "r");
    } else if (mode == "rl") {
        Node* y = z->right;
        z->right = rotateNode(y, "r");
        z = rotateNode(z, "l");
    } else if (mode == "rr") {
        z = rotateNode(z, "l");
    }
    return z;
}

void printBT(const std::string& prefix, const Node* node, bool isLeft)
{
    if( node != nullptr )
    {
        std::cout << prefix;

        std::cout << (isLeft ? "├──" : "└──" );

        // print the value of the node
        std::cout << node->data << std::endl;

        // enter the next tree level - left and right branch
        printBT( prefix + (isLeft ? "│   " : "    "), node->left, true);
        printBT( prefix + (isLeft ? "│   " : "    "), node->right, false);
    }
}

/*You are required to complete this method */
Node* insertToAVL( Node* node, int data)
{
    //Your code here
    /*
     * 1. insert using BST way
     * 2. update current node height, current node must be one of the ancestor
     * 3. compute tree diff (balance factor)
     * 4. if balance factor is larger than 1, 
     *    right left or right right.
     *    if inserted data is larger than right subtree root, right right
     * 5. if balance factor is less than -1, 
     *    left left or left right. 
     *    if inserted data is less than left subtree root, left, left
     * 6. rotation follow the rule
     * */

    /* 1. BST insertion*/
    // Normal B-Tree insertion
    if (node == nullptr) {  // if empty Tree
        node = new Node();
        node->data = data;
    } else {  // insert left or right
        if (data < node->data) {  // go left
            node->left = \
                insertToAVL(node->left, data);
        } else if (data == node->data) {
            // do nothing
        } else{  // go right
            node->right = \
                insertToAVL(node->right, data);
        }
    }
    /* 2. update current node height */
    node->height = heigh(node);
    /* 3. balance factor */
    int lh, rh;
    if (node->left == nullptr) {
        lh = 0;
    } else {
        lh = node->left->height;
    }
    if (node->right == nullptr) {
        rh = 0;
    } else {
        rh = node->right->height;
    }
    int balanceFactor = rh - lh;
    /* 4. if balance factor is larger than 1,
     * right left or right right.
     * if inserted data is larger than
     * right subtree root, right right
     */
    string mode="n";
    if (balanceFactor > 1) {
        /* rl or rr */
        int rd = node->right == nullptr
                ? 0: node->right->data;
        if (data > rd) {
            mode = "rr";
        } else {
            mode = "rl";
        }
    }
    /* 5. if balance factor is less than -1,
     *    left left or left right.
     *    if inserted data is less than
     *    left subtree root, left, left
     */
    if (balanceFactor < -1) {
        int ld = node->left == nullptr
                 ? 0: node->left->data;
        if (data < ld) {
            mode = "ll";
        } else {
            mode = "lr";
        }
    }
    /* 6. rotation
     * since only current node is rotated
     * we can reassign during rotation
     * */
    if (!isBalanced(node)) {
//        cout << "before balance" << endl;
//        printBT("", node, false);
        node = balanceNode(node, mode);
        /*TODO: update height, necessary? */
//        node->height = heigh(node);
//        cout << "after balance" << endl;
//        printBT("", node, false);
//        cout << "balance worked?"
//             << isBalanced(node) << endl;
    }
    return node;
}