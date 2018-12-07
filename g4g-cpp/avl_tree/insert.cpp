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


/* ********************** */
void
(const std::string& prefix, const Node* node, bool isLeft)
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

void rotateNode(Node* z, const string& mode);
void balanceNode(Node* z, Node* y, Node* x, const string& mode);


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

    if (lh > 0) {
        curr->left->height = lh;
    }
    if (rh > 0) {
        curr->right->height = rh;
    }

    if (abs(lh-rh) > 1) {
        return curr;
    }
    /* TODO: Do not need to check childs
     * insertAVL is revursive*/
//    curr = step_goto(curr, target);
//    return findUnbalanced(curr, target);
    return nullptr;
}

void rotateNode(Node* z, const string& mode) {
    if (mode == "r") {
        /* ll condition */
        Node* zCopy = new Node();
        zCopy->left = z->left;
        zCopy->right = z->right;
        zCopy->data = z->data;

        Node* y = zCopy->left;
        Node* t3 = y->right;

        y->right = zCopy;
        zCopy->left = t3;

        z->left = y->left;
        z->right = y->right;
        z->data = y->data;
    } else {  // mode == "l"
        Node* zCopy = new Node();
        zCopy->left = z->left;
        zCopy->right = z->right;
        zCopy->data = z->data;

        Node* y = zCopy->right;
        Node* t2 = y->left;

        y->left = zCopy;
        zCopy->right = t2;

        z->left = y->left;
        z->right = y->right;
        z->data = y->data;
    }
}
void balanceNode(Node* z, Node* y, Node* x, const string& mode) {
    if (mode == "ll") {
        rotateNode(z, "r");
    } else if (mode == "lr") {
        rotateNode(y, "l");
        rotateNode(z, "r");
    } else if (mode == "rl") {
        rotateNode(y, "r");
        rotateNode(z, "l");
    } else if (mode == "rr") {
        rotateNode(z, "l");
    }
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
    // find first unbalanced node
    struct Node* z = findUnbalanced(node, data);
    if (z == nullptr) {
        // no unbalanced node found
        return node;
    }
    /* check height of following node */
    string mode;
    Node* y;
    Node* x;
    if (data > z->data) {
        y = z->right;
        /* right */
        if (data > y->data) {
            x = y->right;
            /* right right */
            mode = "rr";
        } else {
            x = y->left;
            mode = "rl";
        }
    } else {
        y = z->left;
        /* right */
        if (data > y->data) {
            x = y->right;
            /* right right */
            mode = "lr";
        } else {
            x = y->left;
            mode = "ll";
        }
    }
    balanceNode(z, y, x, mode);
    return node;
}


/* ********************** */









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
            printBT("", root, false);
            if(!isBalanced(root)){
                f=false;
                break;
            }
        }
//    cout << "I_:" << I_(root) << endl;
        // traverse
        traverse(root);
        cout << endl;

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
            cout<<"True"<<endl;
        else {
            cout<<"False"<<endl;
            break;
        }
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


void traverse(Node* root) {
    if (root->left != nullptr) {
        traverse(root->left);
    }

    cout << root->data << ", ";

    if (root->right != nullptr) {
        traverse(root->right);
    }
}
