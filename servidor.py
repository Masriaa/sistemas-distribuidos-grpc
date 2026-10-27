# Servidor gRPC

from concurrent import futures
import grpc

import calculadora_pb2
import calculadora_pb2_grpc

class CalculadoraServicer(
    calculadora_pb2_grpc.CalculadoraServicer
):
    def Somar(self, request, context):
        resposta = request.numero1 + request.numero2 + request.numero3

        return calculadora_pb2.OperacaoResponse(
            resultado=resposta
        )

    def Subtrair(self, request, context):
            resposta = request.numero1 - request.numero2 - request.numero3
    
            return calculadora_pb2.OperacaoResponse(
                resultado=resposta
            )

    def Multiplicar(self, request, context):
            resposta = request.numero1 * request.numero2 * request.numero3
    
            return calculadora_pb2.OperacaoResponse(
                resultado=resposta
            )

    def Dividir(self, request, context):
            resposta = request.numero1 / request.numero2 / request.numero3
    
            return calculadora_pb2.OperacaoResponse(
                resultado=resposta
            )

server = grpc.server(
    futures.ThreadPoolExecutor(max_workers=10)
)

calculadora_pb2_grpc.add_CalculadoraServicer_to_server(
    CalculadoraServicer(), server
)

server.add_insecure_port("localhost:50051")
server.start()

print("Servidor gRPC iniciado na porta 50051")

server.wait_for_termination()