#include "cuda_runtime.h" // CUDA����ʱAPI
#include <stdio.h> // ��׼�������

__global__ void helloFromGPU(void) // GPU�˺���
{
	printf("Hello World from GPU!\n"); //���Hello World from GPU!
}

int main(void) // ������
{
	// hello from cpu
	printf("Hello World from GPU!\n"); //CPU���������Hello World from CPU!

	helloFromGPU<<<1,10>>>(); // ����GPU�˺�����10���߳̿飬1��ʾÿ��grid��ֻ��1��block��10��ʾÿ��block����10���߳�
	cudaDeviceReset(); // ���õ�ǰ�豸�ϵ�������Դ״̬����յ�ǰ�豸�ϵ������ڴ�

	return 0;
}