from ipykernel.kernelbase import Kernel


class MyEchoKernel(Kernel):
    implementation = "Echo"
    implementation_version = '1.0'
    language = 'NO-OP'
    language_version = "na"
    language_info = {
        'name': 'Any String',
        'mimetype': 'text/plain',
        'file_extension': '.txt'
    }

    banner = 'My Echo kernel - fun learning!!'

    def do_execute(self, code, silent, store_history=True,
                   user_expressions=None, allow_stdin=False):
        if not silent:
            print("executing code:{}".format(code))
            stream_content = {'name': 'stdout', 'text': code}
            self.send_response(self.iopub_socket, 'stream', stream_content)
            print("done sending response...")
        return {
            'status': 'ok',
            'execution_count': self.execution_count,
            'payload': [],
            'user_expression': {}
        }

    def do_shutdown(self, restart):
        print("trigger shutdown....")
        return super(MyEchoKernel, self).do_shutdown(restart)


def test():
    print("testing my kernel file.")


if __name__ == '__main__':
    test()
    from ipykernel.kernelapp import IPKernelApp

    print("Launching MyEcho kernel.....")
    IPKernelApp.launch_instance(kerel_class=MyEchoKernel)
