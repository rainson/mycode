# Restricted boltzmann machine

The visible layer is vector $\mathbf{x}$ with $n_{vis}$ elements, the hidden layer is vector $\mathbf{h}$ with $m_{hid}$, the visible bias is $\mathbf{a}$, the hidden bias is $\mathbf{b}$ and the weight matrix is  $\mathbf{W}$ with the shape $(n_{vis},~ m_{hid})$. 
### The energy of rbm network is :
\begin{equation}
E(\mathbf{x}, \mathbf{h})=\mathbf{a} \cdot \mathbf{x}^T + \mathbf{x} \cdot \mathbf{W}\cdot \mathbf{h}^T +\mathbf{h} \cdot \mathbf{b}^T
=\sum_{i}{ a_i x_i} + \sum_j{b_j h_j}+ \sum_{i,j}{a_i W_{ij}h_j}
\end{equation}

