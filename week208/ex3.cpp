class Node
{
public:
    string name;
    Node *firstChild;
    Node *nextSibling;
    bool death;
    Node(string name)
    {
        this->name = name;
        this->firstChild = NULL;
        this->nextSibling = NULL;
        this->death = false;
    }
};

class ThroneInheritance
{
public:
    Node *root;
    map<string, Node*> hash;
    ThroneInheritance(string kingName)
    {
        root = new Node(kingName);
        hash[kingName] = root;
    }

    void birth(string parentName, string childName)
    {
        Node *parent = find(parentName);
        if (parent->firstChild == NULL)
        {
            Node *newChild = new Node(childName);
            parent->firstChild = newChild;
            hash[childName] = newChild;
        }
        else
        {
            Node *child = parent->firstChild;
            while (child->nextSibling != NULL)
                child = child->nextSibling;
            Node *newChild = new Node(childName);
            child->nextSibling = newChild;
            hash[childName] = newChild;
        }
    }

    Node *find(string x)
    {
        return hash[x];
    }

    void death(string name)
    {
        Node *deathPerson = find(name);
        deathPerson->death = true;
    }

    vector<string> getInheritanceOrder()
    {
        vector<string> order;
        travel(root, order);
        return order;
    }

    void travel(Node *root, vector<string> &order)
    {
        if (root == NULL)
            return;
        if (!root->death)
            order.push_back(root->name);
        travel(root->firstChild, order);
        travel(root->nextSibling, order);
    }
};
