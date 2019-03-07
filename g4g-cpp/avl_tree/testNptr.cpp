//
// Created by gaojx on 11/30/2018.
//
#include <iostream>

struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};
using namespace std;

Node* assign(Node* node) {
    if (node == nullptr) {
        node = new Node();
    }
    return node;
}

int main() {
    cout << "Hello!" << endl;
    // init root
    Node* root = new Node();
    root->data = 1;

    // init left
    if (root->left == nullptr) {
        cout << "left is nullptr" << endl;
    }
    root->left = new Node();
}