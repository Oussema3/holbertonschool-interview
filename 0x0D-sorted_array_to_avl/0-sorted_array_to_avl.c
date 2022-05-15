#include <stdlib.h>
#include <stdio.h>
#include "binary_trees.h"

/**
 * binary_tree_node - creates a binary tree node
 * @parent: pointer to the parent node of the node to create
 * @value: the value to put in the new node
 * Return: binary tree
 */
avl_t *binary_tree_node(avl_t *parent, int value)
{
  avl_t *tmp = malloc(sizeof(avl_t));

  if (!tmp)
    return (NULL);

  tmp->n = value;
  tmp->left = tmp->right = NULL;
  tmp->parent = parent;
  return (tmp);
}
/**
 * insert - recursive insert nodes
 * @root: pointer to the parent node of the node to create
 * @array: a pointer to the first
 * ******* element of the array to be converted
 * @left: index to the array left extreem
 * @right: index to the array right extreem
 * Return: avl tree
 */
avl_t *insert(avl_t *root, int *array, int left, int right)
{
  avl_t *tmp;
  int i;

  if (left > right)
    return (NULL);
  i = (right + left) / 2;
  tmp = binary_tree_node(root, array[i]);
  if (!tmp)
    return (NULL);
  tmp->left = insert(tmp, array, left, i - 1);
  tmp->right = insert(tmp, array, i + 1, right);
  return (tmp);
}
/**
 * sorted_array_to_avl - create avl tree from sorted array
 *
 * @array: a pointer to the first
 * ******* element of the array to be converted
 * @size: the number of element in the array
 * Return: a pointer to the root node of the
 * ******* created AVL tree, or NULL on failure
 */
avl_t *sorted_array_to_avl(int *array, size_t size)
{
  avl_t *root = NULL;
  size_t left, right;

  if (!array || size <= 0)
    return (NULL);
  left = 0;
  right = size - 1;
  root = insert(root, array, left, right);
  return (root);
}
