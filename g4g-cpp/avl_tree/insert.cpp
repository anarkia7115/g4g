#include<bits/stdc++.h>
using namespace std;
struct Node
{
    int data;
    struct Node *left;
    struct Node *right;
    int height;
};
void traverse(Node* root);
int heigh(struct Node* Node)
{
    /* base case tree is empty */
    if(Node == nullptr)
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
    if(root == nullptr)
        return true;

    /* Get the height of left and right sub trees */
    lh = heigh(root->left);
    rh = heigh(root->right);

    if( abs(lh-rh) <= 1 &&
        isBalanced(root->left) &&
        isBalanced(root->right))
        return true;

    /* If we reach here then tree is not height-balanced */
    return false;
}

struct Node* step_goto(struct Node* curr, int target) {
    if(target > curr->data) {
        curr = curr->right;
    } else {
        curr = curr->left;
    }
    return curr;
}

struct Node* findUnbalanced(struct Node *root, int target)
{
    int lh; /* for height of left subtree */
    int rh; /* for height of right subtree */

    /* If tree is empty then return true */
    if(root == nullptr)
        return nullptr;

    struct Node* curr = root;
    /* Get the height of left and right sub trees */
    lh = heigh(curr->left);
    rh = heigh(curr->right);
    curr->left->height = lh;
    curr->right->height = rh;

    /* find unbalanced node */
    while(abs(lh-rh) <= 1) {
        curr = step_goto(curr, target);
        lh = heigh(curr->left);
        rh = heigh(curr->right);
        curr->left->height = lh;
        curr->right->height = rh;
    }
    /* now curr is the unbalanced node */
    struct Node* w = curr;
//    curr = step_goto(curr, target);
//    struct Node* y = curr;
//    curr = step_goto(curr, target);
//    struct Node* x = curr;
    return w;
}

/* UTILITY FUNCTIONS TO TEST isBalanced() FUNCTION */

/* returns maximum of two integers */


/*  The function Compute the "height" of a tree. Height is the
    number of Nodes along the longest path from the root Node
    down to the farthest leaf Node.*/
int _B_(Node *root)
{
    if(root==nullptr)
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
    static struct Node *prev = nullptr;

    if (root)
    {
        if (!I_(root->left))  // left is null or meet the following condition
            return false;

        if (prev != nullptr && root->data <= prev->data)
            return false;

        prev = root;

        return I_(root->right);
    }

    return true;
}
Node* rotateNode(Node* node, const string& mode);
Node* balanceNode(Node* z, Node* y, Node* x, const string& mode);
Node* insertToAVL(Node* node, int data);
vector<int> z;
void inorder(Node *root)
{
//	z.clear();
    if(root==nullptr)
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
        Node *root = nullptr;
        bool f= true;
        vector<int> a;
        while(q--)
        {
            int k;
            cin>>k;
            a.push_back(k);
            root = insertToAVL(root,k);
//            if(!isBalanced(root)){
//                f=false;
//                break;
//            }
        }
//    cout << "I_:" << I_(root) << endl;
        // traverse
        traverse(root);
//    cout << endl;

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
            cout<<"in order"<<endl;
        else
            cout<<"dis order"<<endl;
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
Node* rotateNode(Node* node, const string& mode) {
    if (mode == "r") {
        /* ll condition */
        Node* z = node;
        Node* y = z->left;
        Node* t3 = y->right;
        y->right = z;
        z->left = t3;
        return y;
    } else {  // mode == "l"
        Node* z = node;
        Node* y = z->right;
        Node* t2 = y->left;
        y->left = z;
        z->right = t2;
        return y;
    }
}
Node* balanceNode(Node* z, Node* y, Node* x, const string& mode) {
   if (mode == "ll") {
       z = rotateNode(z, 'r');
   } else if (mode == "lr") {
       y = rotateNode(y, 'l');
       z->left = y;
       z = rotateNode(z, 'r');
   } else if (mode == "rl") {
       z = rotateNode(z, 'l');
   } else if (mode == "rr") {
       y = rotateNode(y, 'r');
       z->right = y;
       z = rotateNode(z, 'l');
   }
   return z;
}

/*You are required to complete this method */
Node* insertToAVL( Node* node, int data)
{
    /*
    insert to AVL
    1. normal B-Tree insertion
    2. find the first unbalanced node
    3. record fstSide, sndSide
    4. rotate
    */
    //Your code here
    // Normal B-Tree insertion
    if (node == nullptr) {  // if empty Tree
        node = new Node();
        node->data = data;
    } else {  // insert left or right
        if (data <= node->data) {  // go left
            node->left = \
                insertToAVL(node->left, data);
        } else {  // go right
            node->right = \
                insertToAVL(node->right, data);
        }
    }
    // find first unbalanced node
    struct Node* z = findUnbalanced(node, data);
    if (z == nullptr) {
        // no unbalanced node found
        return node;
    }
    /* check height of following node */
    if (data > z->data) {
        struct Node* y = w->right;
        /* right */
        if (data > y->data) {
            struct Node* x = y->right;
            /* right */
            rotate()
        }
    } else
    return node;
}

void traverse(Node* root) {
    if (root->left != nullptr) {
        traverse(root->left);
    }

    cout << root->data << ", ";

    if (root->right != nullptr) {
        traverse(root->right);
    }
}
